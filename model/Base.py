
from datetime import datetime
from typing import List
from sqlalchemy import Column,  String, TEXT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import DateTime, Integer

Base = declarative_base()
# messageHisotry = Table(
#     'message_history', Base.metadata,
#     Column('id', String(64)),
#     Column('date', DateTime),
# )
# messageItem = Table(
#     'message_item', Base.metadata,
#     Column('id', String(64)),
#     Column('type', String(64)),
#     Column('message_id', String(64)),
#     Column('content', Text)
# )


class MessageHistoryElement(Base):
    __tablename__ = 'message_history_element'
    _id = Column('id', String(64), primary_key=True)
    _message_id = Column('message_id', String(64))
    _type = Column('type', String(64))
    _content = Column('content', TEXT)
    _sort_num = Column('sort_num', Integer)

    @property
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, id: str):
        self._id = id

    @property
    def message_id(self) -> str:
        return self._message_id

    @message_id.setter
    def message_id(self, message_id: str):
        self._message_id = message_id

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, type: str):
        self._type = type

    @property
    def content(self) -> str:
        return self._content

    @content.setter
    def content(self, content: str):
        self._content = content

    @property
    def sort_num(self) -> int:
        return self._sort_num

    @sort_num.setter
    def sort_num(self, sort_num: int):
        self._sort_num = sort_num


class MessageHistory(Base):
    __tablename__ = 'message_history'
    _id = Column('id', String(64), primary_key=True)
    _type = Column("type", String(40))
    _message_date = Column('message_date', DateTime)
    _sender_id = Column('sender_id', String(64), primary_key=True)
    _sender_type = Column('sender_type', String(64), primary_key=True)
    _receiver_id = Column('receiver_id', String(64), primary_key=True)
    _receiver_type = Column('receiver_type', String(64), primary_key=True)
    _elements = None

    @property
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, id: str):
        self._id = id

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, type: str):
        self._type = type

    @property
    def message_date(self) -> datetime:
        return self._message_date

    @message_date.setter
    def message_date(self, message_date: datetime):
        self._message_date = message_date

    @property
    def sender_id(self) -> str:
        return self._sender_id

    @sender_id.setter
    def sender_id(self, sender_id: str):
        self._sender_id = sender_id

    @property
    def sender_type(self) -> str:
        return self._sender_type

    @sender_type.setter
    def sender_type(self, sender_type: str):
        self._sender_type = sender_type

    @property
    def receiver_id(self) -> str:
        return self._receiver_id

    @receiver_id.setter
    def receiver_id(self, receiver_id: str):
        self._receiver_id = receiver_id

    @property
    def receiver_type(self) -> str:
        return self._receiver_type

    @receiver_type.setter
    def receiver_type(self, receiver_type: str):
        self._receiver_type = receiver_type

    @property
    def elements(self) -> List[MessageHistoryElement]:
        return self._elements

    @elements.setter
    def elements(self, elements: List[MessageHistoryElement]):
        self._elements = elements
