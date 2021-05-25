#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
主窗口
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget


if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(1000, 550)
    w.move(300, 300)
    w.setWindowTitle('enjoy')
    w.show()

    sys.exit(app.exec_())
