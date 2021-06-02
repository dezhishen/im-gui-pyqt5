#!/usr/bin/python3
# -*- coding: utf-8 -*-

from lib.im.im_instance.MessageSenderInstance import MessageSenderInstance
import sys
from PyQt5 import QtSvg
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import (QTextEdit, QToolBar, QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication)


class ChatInput(QWidget):

    __toolbar = None
    __textEdit = None
    __message_send_handler = None

    def __init__(self, message_send_handler: MessageSenderInstance):
        super().__init__()
        self.__message_send_handler = message_send_handler
        self.initUI()

    def initUI(self):
        # toolbar
        toolbar = QToolBar()
        imageSvg = QtSvg.QSvgWidget("./assets/icons/tupian.svg")
        imageSvg.setMaximumSize(QSize(20, 20))
        toolbar.addWidget(imageSvg)
        self.__toolbar = toolbar
        # 按钮组
        closeButton = QPushButton("关闭")
        sendButton = QPushButton("发送")
        bottonsHbox = QHBoxLayout()
        bottonsHbox.addStretch(1)
        bottonsHbox.addWidget(closeButton)
        bottonsHbox.addWidget(sendButton)
        mainBox = QVBoxLayout()
        mainBox.addWidget(toolbar)
        textEdit = QTextEdit()
        textEdit.setAcceptRichText(False)
        self.__textEdit = textEdit
        mainBox.addWidget(textEdit)
        # mainBox.addStretch(1)
        mainBox.addLayout(bottonsHbox)
        self.setLayout(mainBox)
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()

    @property
    def textEdit(self):
        return self.__textEdit

    @property
    def toolbar(self):
        return self.__toolbar

    @property
    def message_sender(self):
        return self.__message_send_handler


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = ChatInput()
    fileSvg = QtSvg.QSvgWidget("./assets/icons/wenjian.svg")
    fileSvg.setMaximumSize(QSize(20, 20))
    ex.getToolbar().addAction()
    sys.exit(app.exec_())
