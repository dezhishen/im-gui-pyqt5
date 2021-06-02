#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtSvg
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import (QTextEdit, QToolBar, QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication)


class ChatRecordBrowser(QWidget):

    _toolbar = None
    _textEdit = None
    _message_send_handler = None

    def __init__(self, message_send_handler):
        super().__init__()
        self._message_send_handler = message_send_handler
        self.initUI()

    def initUI(self):
        # toolbar
        toolbar = QToolBar()
        imageSvg = QtSvg.QSvgWidget("./assets/icons/tupian.svg")
        imageSvg.setMaximumSize(QSize(20, 20))
        toolbar.addWidget(imageSvg)
        self._toolbar = toolbar
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
        self._textEdit = textEdit
        mainBox.addWidget(textEdit)
        # mainBox.addStretch(1)
        mainBox.addLayout(bottonsHbox)
        self.setLayout(mainBox)
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()

    def getTextEdit(self):
        return self._textEdit

    def getToolbar(self):
        return self._toolbar


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = ChatRecordBrowser()
    fileSvg = QtSvg.QSvgWidget("./assets/icons/wenjian.svg")
    fileSvg.setMaximumSize(QSize(20, 20))
    ex.getToolbar().addWidget(fileSvg)
    sys.exit(app.exec_())
