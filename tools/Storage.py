
from sqlite3.dbapi2 import Connection, Cursor
import threading
import sqlite3
from datetime import datetime
from typing import List
from model.Base import MessageHistory, MessageHistoryElement
import uuid

sqlite_mutex = threading.Lock()

db_dir = "./resources/db/message.db"


class _MessageHistoryElementStorage:
    _conn: Connection = None

    def __init__(self, conn: Connection) -> None:
        self._conn = conn

    def insert(self,
               cursor: Cursor,
               message_id: str,
               elements: List[MessageHistoryElement]):
        args = []
        sql = """
            insert into message_history_element(
                id,
                message_id,
                type,
                content,
                sort_num
                )values
        """
        for i in range(len(elements)):
            e = elements[i]
            if e.id is None:
                e.id = str(uuid.uuid1()).replace("-", "")
            e.message_id = message_id
            e.sort_num = i
            sql += "(?,?,?,?,?)"
            if i < len(elements)-1:
                sql += ","
            args.append(e.id)
            args.append(e.message_id)
            args.append(e.type)
            args.append(e.content)
            args.append(e.sort_num)
        cursor.execute(sql, args)

    def query(self, message_id: str) -> List[MessageHistoryElement]:
        sql = """
        select id,message_id,type,content,sort_num
          from message_history_element
         where message_id = ?
         order by sort_num asc
        """
        cursor = self._conn.cursor()
        cursor.execute(sql, [message_id])
        values = cursor.fetchall()
        cursor.close()
        result = []
        for v in values:
            e = MessageHistoryElement()
            e.id = v[0]
            e.message_id = v[1]
            e.type = v[2]
            e.content = v[3]
            e.sort_num = v[4]
            result.append(e)
        return result


class _MessageHistoryStorage:
    _conn: Connection = None
    _element: _MessageHistoryElementStorage = None

    def __init__(self) -> None:
        self._conn = sqlite3.connect(db_dir, check_same_thread=False)
        self._element = _MessageHistoryElementStorage(self._conn)

    def insert(self, message_history: MessageHistory):
        sql = """
        insert into message_history(
            id,
            type,
            sender_type,
            sender_id,
            message_date,
            receiver_type,
            receiver_id
        )values(?,?,?,?,?,?,?)
        """
        if message_history.id is None:
            message_history.id = str(uuid.uuid1()).replace("-", "")
        if message_history.type is None:
            message_history.type = "recieve"
        cursor = self._conn.cursor()
        cursor.execute("BEGIN TRANSACTION")
        cursor.execute(
            sql, (
                message_history.id,
                message_history.type,
                message_history.sender_type,
                message_history.sender_id,
                message_history.message_date,
                message_history.receiver_type,
                message_history.receiver_id
            )
        )
        self._element.insert(
            cursor=cursor,
            message_id=message_history.id,
            elements=message_history.elements
        )
        cursor.execute("COMMIT")

    def query(
            self,
            start_time: datetime = None,
            end_time: datetime = None,
            receiver_id: str = None,
            receiver_type: str = None,
            sender_id: str = None,
            sender_type: str = None,
            limit: int = 30
    ) -> List[MessageHistory]:

        where_condition = " where 1 = 1"
        args = []
        if start_time is not None:
            where_condition = " and message_date >= ?"
            args.append(start_time)
        if end_time is not None:
            where_condition = " and message_date <= ?"
            args.append(end_time)
        if receiver_id is not None:
            where_condition = " and receiver_id = ?"
            args.append(receiver_id)
        if receiver_type is not None:
            where_condition = " and receiver_type = ?"
            args.append(receiver_type)
        if sender_id is not None:
            where_condition = " and sender_id = ?"
            args.append(sender_id)
        if sender_type is not None:
            where_condition = " and sender_type = ?"
            args.append(sender_type)
        where_condition = " limit ?"
        args.append(limit)
        cursor = self._conn.cursor()
        sql = "select \
                id,\
                type,\
                sender_type,\
                sender_id,\
                message_date,\
                receiver_type, \
                receiver_id\
            from message_history"+where_condition
        cursor.execute(sql, args)
        values = cursor.fetchall()
        cursor.close()
        result = []
        for v in values:
            e = MessageHistory()
            e.id = v[0]
            e.type = v[1]
            e.sender_type = v[2]
            e.sender_id = v[3]
            e.message_date = v[4]
            e.receiver_type = v[5]
            e.receiver_id = v[6]
            e.elements = self._element.query(message_id=e.id)
            result.append(e)
        return result


MESSAGE_HISTORY_STORAGE = _MessageHistoryStorage()
