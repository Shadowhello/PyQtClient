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
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout

from Libraries.Widgets.ContentWidget import ContentWidget
from Libraries.Widgets.FramelessWindow import FramelessWindow
from Libraries.Widgets.LinkWidget import LinkWidget
from Libraries.Widgets.MenuWidget import MenuWidget
from Libraries.Widgets.TitleWidget import TitleWidget


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
        # 左侧菜单栏和右侧内容栏
        self._initView()

    def showNormalBtn(self, visible):
        self._titleBar.showNormalBtn(visible)

    def _initTitleBar(self):
        '''标题栏'''
        parent = self.parent() or self.parentWidget() or self
        self._titleBar = TitleWidget(self)
        self._titleBar.minimized.connect(parent.showMinimized)
        self._titleBar.maximized.connect(parent.showMaximized)
        self._titleBar.normaled.connect(parent.showNormal)
        self._titleBar.closed.connect(parent.close)
        self.layout().addWidget(self._titleBar)

    def _initView(self):
        '''左侧菜单栏和右侧内容栏'''
        layout = QHBoxLayout()
        layout.addWidget(MenuWidget(self))
        layout.addWidget(LinkWidget(self))
        layout.addWidget(ContentWidget(self))
        self.layout().addLayout(layout)


class MainWindow(FramelessWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        layout = QVBoxLayout(self, spacing=0)
        layout.setContentsMargins(0, 0, 0, 0)
        self._mainWidget = MainWidget(self)
        layout.addWidget(self._mainWidget)

    def changeEvent(self, event):
        super(MainWindow, self).changeEvent(event)
        if event.type() == QEvent.WindowStateChange:
            self._mainWidget.showNormalBtn(
                self.windowState() == Qt.WindowMaximized)


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
    w = MainWindow()
    w.resize(800, 600)
    w.show()
    sys.exit(app.exec_())
