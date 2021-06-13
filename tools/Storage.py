
import threading
import sqlite3
from datetime import datetime
from typing import List
from model.Base import MessageHistory

sqlite_mutex = threading.Lock()

db_dir = "./im.db"


class _MessageHistoryStorage:
    _conn = None

    def __init__(self) -> None:
        self._conn = sqlite3.connect(db_dir, check_same_thread=False)

    def insert(self):
        pass

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
                sender_type,\
                sender_id,\
                message_date,\
                receiver_id,\
                receiver_type \
            from message_history"+where_condition
        cursor.execute(sql, args)
        values = cursor.fetchall()
        result = []
        for v in values:
            e = MessageHistory()
            e.id = v[0]
            e.sender_type = v[1]
            result.append(e)
        cursor.close()
        return result


MESSAGE_HISTORY_STORAGE = _MessageHistoryStorage()
