# from event.MessageSignal import MESSAGE_SIGNAL
# from remote.Entity import Mine, Receiver, Sender
# from remote.Message import Message, MessageElement
from event.MessageSignal import MESSAGE_SIGNAL
from remote.Entity import Mine, Receiver, Sender
from remote.Message import Message, MessageElement
from remote.Client import Client
from tools.ThreadPoolUtil import THREAD_POOL
from ws4py.client.threadedclient import WebSocketClient
import requests
import json


class DummyClient(WebSocketClient):
    def opened(self):
        print("opend")
        pass
        # self.send("www.baidu.com")

    def closed(self, code, reason=None):
        print("close")
        print(code)
        print(reason)
        pass
        # print "Closed down", code, reason

    def received_message(self, m):
        print(m)
        dict = json.loads(m.data)
        if dict['post_type'] == "message":
            sender = Sender(
                id=dict['sender']['user_id'],
                type=dict['post_type'],
                code="1",
                name=dict['sender']['nickname'],
                alias_name=dict['sender']['card'],
                header_image_url="https://avatars.githubusercontent.com/u/" +
                "26274059?v=4"
            )
            receiver = Receiver(id=1,
                                type="pri",
                                code="1",
                                name="a",
                                alias_name="别名",
                                meta={"headerImageUrl": "test"})
            elements = [
                MessageElement(
                    id=None,
                    type="text",
                    content=bytes(dict['raw_message'], encoding="utf-8"))
            ]
            msg = Message(id=None, sender=sender,
                          receiver=receiver, elements=elements)
            MESSAGE_SIGNAL.receive.emit(msg)


class CqWsClient(Client):
    def _send_message(self, message: Message):
        for element in message.elements:
            url = "http://127.0.0.1:5700/send_private_msg?user_id="\
                + "601556811&message=" + \
                str(element.content, encoding="utf-8")
            print(url)
            requests.get(url)
        return message

    def _listen_receive_message(self):
        """监听方法
        """
        THREAD_POOL.submit(self.__listen_message)
        # wait([f], return_when=ALL_COMPLETED)
        # pass

    def _login(self, mine: Mine):
        return mine

    def __listen_message(self):
        try:
            ws = DummyClient('ws://127.0.0.1:6700/')
            ws.connect()
            ws.run_forever()
        except Exception as e:
            print(e)
            ws.close()
