#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2018年2月6日
@author: Irony."[讽刺]
@site: http://alyl.vip, http://orzorz.vip, https://coding.net/u/892768447, https://github.com/892768447
@email: 892768447@qq.com
@file: Libraries.Widgets.MainWidget
@description: 
'''
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QSpacerItem,\
    QSizePolicy, QPushButton, QProgressBar


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2018 Irony.\"[讽刺]"
__Version__ = "Version 1.0"


class MainWidget(QWidget):

    def __init__(self, *args, **kwargs):
        super(MainWidget, self).__init__(*args, **kwargs)
        # 保证qss有效
        self.setAttribute(Qt.WA_StyledBackground, True)
        layout = QVBoxLayout(self, spacing=0)
        layout.setContentsMargins(0, 0, 0, 0)
        # 标题栏
        self._initTitleBar()
        # 进度条
        self._initProgressBar()
        # 左侧菜单栏和右侧内容栏
        self._initView()

    def _initTitleBar(self):
        '''标题栏'''
        layout = QHBoxLayout()
        # 左侧空白拉伸
        layout.addItem(QSpacerItem(
            20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        layout.addWidget(QPushButton("", self, objectName="minimumButton"))
        layout.addWidget(QPushButton("", self, objectName="maximumButton"))
        layout.addWidget(QPushButton("", self, objectName="normalButton"))
        layout.addWidget(QPushButton("", self, objectName="closeButton"))
        self.layout().addLayout(layout)

    def _initProgressBar(self):
        '''进度条'''
        self._progressBar = QProgressBar(self, textVisible=False)
        self.layout().addWidget(self._progressBar)

    def _initView(self):
        '''左侧菜单栏和右侧内容栏'''
        layout = QHBoxLayout()
        layout.addWidget(QWidget(self))
        layout.addWidget(QWidget(self))
        self.layout().addLayout(layout)


if __name__ == "__main__":
    import sys
    import os
    os.chdir("../../")
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtGui import QFontDatabase
    app = QApplication(sys.argv)
    QFontDatabase.addApplicationFont("themes/default/font.ttf")
    app.setStyleSheet(open("themes/default/style.qss",
                           "rb").read().decode("utf-8"))
    w = MainWidget()
    w.resize(800, 600)
    w.show()
    sys.exit(app.exec_())
