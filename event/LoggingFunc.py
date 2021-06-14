
from event.MessageSignal import MESSAGE_SIGNAL
from remote.Message import Message
import logging
logging.basicConfig(
    level=logging.DEBUG,
    filename=r'./logs/message.log',
    format="%(asctime)s %(name)s %(levelname)s %(message)s",
    datefmt='%Y-%m-%d  %H:%M:%S %a'
)


def connect_log():
    MESSAGE_SIGNAL.receive.connect(logging_receive)
    MESSAGE_SIGNAL.after_send.connect(logging_send)


def logging_receive(message: Message):
    logging.debug("receive a message from %s-%s",
                  message.sender.type, message.sender.id)


def logging_send(message: Message):
    logging.debug("send a message to %s-%s",
                  message.receiver.type, message.receiver.id)
