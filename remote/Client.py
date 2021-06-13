from abc import abstractmethod
from event.FriendsGroupsSignal import FRIENDS_GROUP_SIGNAL
from event.MessageSignal import MESSAGE_SIGNAL
from event.LoginSignal import LOGIN_SIGNAL
from typing import List
from remote.Message import Message
from remote.Entity import Entity, Mine


class Client(object):
    _mine = None
    _friends = None
    _groups = None

    def __init__(self) -> None:
        super().__init__()
        # 登录相关信号绑定
        LOGIN_SIGNAL.login.connect(self.do_login)
        LOGIN_SIGNAL.logout.connect(self.do_logout)
        LOGIN_SIGNAL.after_login_success.connect(self.do_refresh_frends)
        LOGIN_SIGNAL.after_login_success.connect(
            self.do_refresh_groups
        )
        LOGIN_SIGNAL.after_login_success.connect(
            self.start_listen_receive_message)
        # 消息相关信号绑定
        # 好友列表相关信号绑定
        FRIENDS_GROUP_SIGNAL.do_load_friends.connect(self.do_refresh_frends)
        FRIENDS_GROUP_SIGNAL.do_load_groups.connect(self.do_refresh_groups)

    @property
    def mine(self) -> Mine:
        return self._mine

    @mine.setter
    def mine(self, mine: Mine):
        self._mine = mine

    @property
    def friends(self) -> List[Entity]:
        return self._friends

    @friends.setter
    def friends(self, friends: List[Entity]):
        self._friends = friends

    @property
    def groups(self) -> List[Entity]:
        return self._groups

    @groups.setter
    def groups(self, groups: List[Entity]):
        self._groups = groups

    def do_login(self, mine: Mine):
        self.mine = self._login(mine)
        LOGIN_SIGNAL.after_login_success.emit(self.mine)

    def do_logout(self, mine: Mine):
        self._logout(mine)
        LOGIN_SIGNAL.after_logout.emit(self.mine)

    def start_listen_receive_message(self):
        self._listen_receive_message()

    def do_refresh_frends(self, mine: Mine):
        self.friends = self._load_friends(mine=mine)
        if self.friends is None:
            self.friends = []
        FRIENDS_GROUP_SIGNAL.after_load_friends.emit(self.friends)

    def do_refresh_groups(self, mine: Mine):
        self.groups = self._load_groups(mine=mine)
        if self.groups is None:
            self.groups = []
        FRIENDS_GROUP_SIGNAL.after_load_groups.emit(self.groups)

    def do_send_message(self, message: Message):
        result = self._send_message(message)
        MESSAGE_SIGNAL.after_send.emit(result)

    @abstractmethod
    def _send_message(self, message: Message) -> Message:
        """发送消息

        Args:
            message (Message): 消息对象
        """
        pass

    @abstractmethod
    def _listen_receive_message(self):
        """监听方法

        Args:
            callback (typing.Callable[[Message], ]): 回调函数,方法内部应该回调该方法,处理消息的接收
        """
        pass

    @abstractmethod
    def _login(self, mine: Mine) -> Mine:
        """登录
        """
        pass

    @abstractmethod
    def _logout(self, mine: Mine):
        """登出
        """
        pass

    @abstractmethod
    def _load_friends(self, mine: Mine) -> List[Entity]:
        pass

    @abstractmethod
    def _load_groups(self, mine: Mine) -> List[Entity]:
        pass
