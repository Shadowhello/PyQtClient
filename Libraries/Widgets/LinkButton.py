#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2018年2月10日
@author: Irony."[讽刺]
@site: http://alyl.vip, http://orzorz.vip, https://coding.net/u/892768447, https://github.com/892768447
@email: 892768447@qq.com
@file: Libraries.Widgets.LinkButton
@description: 
'''
import webbrowser

from PyQt5.QtCore import QTimer, pyqtProperty, QRectF, Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QPushButton, QGraphicsDropShadowEffect, QWidget,\
    QStylePainter, QStyleOptionButton, QStyle


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2018 Irony.\"[讽刺]"
__Version__ = "Version 1.0"


class LinkButton(QPushButton):

    def __init__(self, *args, **kwargs):
        super(LinkButton, self).__init__(*args, **kwargs)
        self.clicked.connect(self.onClicked)
        self.setCursor(Qt.PointingHandCursor)
        self._rotate = 0
        self._radius = 0
        self._step = 45
        self._padding = 10
        self._url = ""
        self._image = ""
        self._shadowColor = "#FFFFFF"
        self._direction = None    # clockwise 顺时针 anticlockwise 逆时针
        self._timer = QTimer(self, timeout=self.update)
        self._effect = QGraphicsDropShadowEffect(self)
        self._effect.setBlurRadius(self._padding * 2)
        self._effect.setOffset(0, 0)

    def __del__(self):
        self.stop()

    def stop(self):
        self._timer.stop()

    def update(self):
        if self._direction == "clockwise":    # 顺时针
            # 0 45 90 135 180 225 270 315 360
            if self._rotate == -360:
                self._rotate = 45
            else:
                self._rotate += self._step
            if self._rotate > 360:    # 旋转一周后停止
                self._rotate = 360
                self._direction = None
                self._timer.stop()    # 停止计时器
            else:
                super(LinkButton, self).update()
        elif self._direction == "anticlockwise":    # 逆时针
            # 360 -45 -90 -135 -180 -225 -270 -315 -360
            if self._rotate == 360:
                self._rotate = -45
            else:
                self._rotate -= self._step
            if self._rotate < -360:
                self._rotate = -360
                self._direction = None
                self._timer.stop()
            else:
                super(LinkButton, self).update()

    def paintEvent(self, event):
        '''绘制事件'''
        if not self._timer.isActive():
            return super(LinkButton, self).paintEvent(event)
        if self._direction in ("clockwise", "anticlockwise"):
            option = QStyleOptionButton()
            self.initStyleOption(option)
            option.text = ""  # 不让其绘制文字
            painter = QStylePainter(self)
            painter.drawControl(QStyle.CE_PushButton, option)
            # 变换坐标为正中间
            painter.translate(self.rect().center())
            painter.rotate(self._rotate)  # 旋转
            fm = self.fontMetrics()
            # 在变换坐标后的正中间画文字
            w = fm.width(self.text())
            h = fm.height()
            painter.drawText(
                QRectF(0 - w * 2, 0 - h, w * 2 * 2, h * 2), Qt.AlignCenter,
                self.text())
            return
        super(LinkButton, self).paintEvent(event)

    def enterEvent(self, event):
        '''鼠标进入事件'''
        self._effect.setColor(QColor(self._shadowColor))
        self._effect.setBlurRadius(self._padding * 2)
        self.setGraphicsEffect(self._effect)
        self._timer.stop()
        self._direction = "clockwise"    # 顺时针旋转
        self._timer.start(60)

    def leaveEvent(self, event):
        '''鼠标离开事件'''
        self._effect.setBlurRadius(0)
        self.setGraphicsEffect(self._effect)
        self._timer.stop()
        self._direction = "anticlockwise"    # 逆时针旋转
        self._timer.start(60)
    
    def onClicked(self):
        if self._url:
            return webbrowser.open_new_tab(self._url)

    def getPadding(self)->int:
        return self._padding

    def setPadding(self, padding):
        self._padding = padding

    def getShadowColor(self)->str:
        return self._shadowColor

    def setShadowColor(self, color: str):
        self._shadowColor = color

    def getImage(self)->str:
        return self._image

    def setImage(self, image: str):
        self._image = image

    def getUrl(self)->str:
        return self._url

    def setUrl(self, url: str):
        self._url = url

    padding = pyqtProperty(int, getPadding, setPadding)
    shadowColor = pyqtProperty(str, getShadowColor, setShadowColor)
    image = pyqtProperty(str, getImage, setImage)
    url = pyqtProperty(str, getUrl, setUrl)


if __name__ == "__main__":
    import sys
    import os
    os.chdir("../../")
    from PyQt5.QtWidgets import QApplication, QVBoxLayout
    from PyQt5.QtGui import QFontDatabase
    app = QApplication(sys.argv)
    QFontDatabase.addApplicationFont("themes/default/font.ttf")
    app.setStyleSheet(open("themes/default/style.qss",
                           "rb").read().decode("utf-8"))
    parent = QWidget(objectName="Widget",
                     styleSheet="#Widget{background: red;}")
    layout = QVBoxLayout(parent)
    layout.setContentsMargins(20, 20, 20, 20)
    layout.addWidget(LinkButton(parent, objectName="qqButton"))
    parent.show()
    sys.exit(app.exec_())
