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
from PyQt5.QtCore import Qt, QEvent, QPropertyAnimation, pyqtSignal, QRect, QEasingCurve, QParallelAnimationGroup
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout

from Libraries.Widgets.ContentWidget import ContentWidget
from Libraries.Widgets.FramelessWindow import FramelessWindow
from Libraries.Widgets.LinkWidget import LinkWidget
from Libraries.Widgets.MenuWidget import MenuWidget
from Libraries.Widgets.TitleWidget import TitleWidget
from Libraries.Widgets.ToolTipWidget import ToolTipWidget


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2018 Irony.\"[讽刺]"
__Version__ = "Version 1.0"


class MainWidget(QWidget):

    showed = pyqtSignal()
    closed = pyqtSignal()
    exited = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(MainWidget, self).__init__(*args, **kwargs)
        self.resize(800, 600)
        # 保证qss有效
        self.setAttribute(Qt.WA_StyledBackground, True)
        # 左侧菜单栏和右侧内容栏
        self._initView()

    def showEvent(self, event):
        super(MainWidget, self).showEvent(event)
        # 动画效果
        self._initAnimations()

    def resizeEvent(self, event):
        super(MainWidget, self).resizeEvent(event)
        if not hasattr(self, "_animationGroupShow"):
            return
        self._initAnimationsValues()

    def onClose(self):
        self._animationGroup.stop()
        self._initAnimationsValues(False)
        self._animationGroup.finished.connect(self.exited.emit)
        self._animationGroup.start()

    def showNormalBtn(self, visible):
        self._titleBar.showNormalBtn(visible)

    def _initView(self):
        '''标题栏'''
        parent = self.parent() or self.parentWidget() or self
        self._titleBar = TitleWidget(parent=self)
        self._titleBar.minimized.connect(parent.showMinimized)
        self._titleBar.maximized.connect(parent.showMaximized)
        self._titleBar.normaled.connect(parent.showNormal)
        self._titleBar.closed.connect(self.onClose)
        '''左侧菜单栏和右侧内容栏'''
        cLayout = QHBoxLayout()
        self._menuWidget = MenuWidget(self)
        self._linkWidget = LinkWidget(self)
        self._contentWidget = ContentWidget(self)
        cLayout.addWidget(self._menuWidget)
        cLayout.addWidget(self._linkWidget)
        cLayout.addWidget(self._contentWidget)
        # 总体布局
        layout = QVBoxLayout(self, spacing=0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self._titleBar)
        layout.addLayout(cLayout)

    def _initAnimations(self):
        '''动画效果'''
        if hasattr(self, "_animationGroup"):
            return  # 由于showEvent的关系,这里要防止多次实例化
        self._animationGroup = QParallelAnimationGroup(self)  # 并行动画
        # 标题栏
        self._animationTitleBar = QPropertyAnimation(
            self._titleBar, b"geometry", self, easingCurve=QEasingCurve.OutBounce, duration=1000)
        # 菜单栏
        self._animationMenuWidget = QPropertyAnimation(
            self._menuWidget, b"geometry", self, easingCurve=QEasingCurve.OutBounce, duration=1000)
        # 链接
        self._animationLinkWidget = QPropertyAnimation(
            self._linkWidget, b"geometry", self, easingCurve=QEasingCurve.OutBounce, duration=1000)
        # 内容
        self._animationContentWidget = QPropertyAnimation(
            self._contentWidget, b"geometry", self, easingCurve=QEasingCurve.OutBounce, duration=1000)
        # add to group
        self._animationGroup.addAnimation(self._animationTitleBar)
        self._animationGroup.addAnimation(self._animationMenuWidget)
        self._animationGroup.addAnimation(self._animationLinkWidget)
        self._animationGroup.addAnimation(self._animationContentWidget)
        # 初始化位置
        self._initAnimationsValues(True)
        # 启动动画效果
        self._animationGroup.start()

    def _initAnimationsValues(self, show=True):
        # 标题栏
        startValue = QRect(self.width(), 0, self._titleBar.width(),
                           self._titleBar.height())
        endValue = QRect(0, 0, self._titleBar.width(),
                         self._titleBar.height())
        self._animationTitleBar.setStartValue(startValue if show else endValue)
        self._animationTitleBar.setEndValue(endValue if show else startValue)

        # 菜单栏
        startValue = QRect(-self._menuWidget.width(), self._titleBar.height(),
                           self._menuWidget.width(), self._menuWidget.height())
        endValue = QRect(0, self._titleBar.height(),
                         self._menuWidget.width(), self._menuWidget.height())
        self._animationMenuWidget.setStartValue(
            startValue if show else endValue)
        self._animationMenuWidget.setEndValue(endValue if show else startValue)

        # 链接
        startValue = QRect(self._menuWidget.width(
        ), -self.height(), self._linkWidget.width(), self._linkWidget.height())
        endValue = QRect(
            self._menuWidget.width(), self._titleBar.height(),
            self._linkWidget.width(), self._linkWidget.height())
        self._animationLinkWidget.setStartValue(
            startValue if show else endValue)
        self._animationLinkWidget.setEndValue(endValue if show else startValue)

        # 内容
        startValue = QRect(self.width(), self.height(), self._contentWidget.width(),
                           self._contentWidget.height())
        endValue = QRect(
            self._menuWidget.width() + self._linkWidget.width(),
            self._titleBar.height(), self._contentWidget.width(),
            self._contentWidget.height())
        self._animationContentWidget.setStartValue(
            startValue if show else endValue)
        self._animationContentWidget.setEndValue(
            endValue if show else startValue)


class MainWindow(FramelessWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.resize(800, 600)
        layout = QVBoxLayout(self, spacing=0)
        layout.setContentsMargins(0, 0, 0, 0)
        self._mainWidget = MainWidget(self)
        self._mainWidget.exited.connect(self.close)
        layout.addWidget(self._mainWidget)
        # tooltip
        ToolTipWidget.instance(self)

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
    w.show()
    sys.exit(app.exec_())