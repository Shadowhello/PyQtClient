#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2018年2月9日
@author: Irony."[讽刺]
@site: http://alyl.vip, http://orzorz.vip, https://coding.net/u/892768447, https://github.com/892768447
@email: 892768447@qq.com
@file: Libraries.Widgets.RubberBandButton
@description: 
'''
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, pyqtProperty,\
    QRectF, QParallelAnimationGroup
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QPushButton, QStylePainter, QStyle,\
    QStyleOptionButton


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2018 Irony.\"[讽刺]"
__Version__ = "Version 1.0"


class RubberBandButton(QPushButton):

    def __init__(self, *args, **kwargs):
        super(RubberBandButton, self).__init__(*args, **kwargs)
        self.setFlat(True)
        self._width = 0
        self._height = 0
        self._bgcolor = "green"

    def paintEvent(self, event):
        self._initAnimate()
        painter = QStylePainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setBrush(QColor(self._bgcolor))
        painter.setPen(QColor(self._bgcolor))
        painter.drawEllipse(QRectF(
            (self.minimumWidth() - self._width) / 2,
            (self.minimumHeight() - self._height) / 2,
            self._width,
            self._height
        ))
        # 绘制本身的文字和图标
        options = QStyleOptionButton()
        options.initFrom(self)
        size = options.rect.size()
        size.transpose()
        options.rect.setSize(size)
        options.features = QStyleOptionButton.Flat
        options.text = self.text()
        options.icon = self.icon()
        options.iconSize = self.iconSize()
        painter.drawControl(QStyle.CE_PushButton, options)
        event.accept()

    def _initAnimate(self):
        if hasattr(self, "animate"):
            return
        self._width = self.minimumWidth() * 7 / 8
        self._height = self.minimumHeight() * 7 / 8
#         self._width=175
#         self._height=175
        wanimate = QPropertyAnimation(self, b"width")
        wanimate.setEasingCurve(QEasingCurve.OutElastic)
        wanimate.setDuration(700)
        wanimate.valueChanged.connect(self.update)
        wanimate.setKeyValueAt(0, self._width)
#         wanimate.setKeyValueAt(0.1, 180)
#         wanimate.setKeyValueAt(0.2, 185)
#         wanimate.setKeyValueAt(0.3, 190)
#         wanimate.setKeyValueAt(0.4, 195)
        wanimate.setKeyValueAt(0.5, self._width + 6)
#         wanimate.setKeyValueAt(0.6, 195)
#         wanimate.setKeyValueAt(0.7, 190)
#         wanimate.setKeyValueAt(0.8, 185)
#         wanimate.setKeyValueAt(0.9, 180)
        wanimate.setKeyValueAt(1, self._width)
        hanimate = QPropertyAnimation(self, b"height")
        hanimate.setEasingCurve(QEasingCurve.OutElastic)
        hanimate.setDuration(700)
        hanimate.setKeyValueAt(0, self._height)
#         hanimate.setKeyValueAt(0.1, 170)
#         hanimate.setKeyValueAt(0.3, 165)
        hanimate.setKeyValueAt(0.5, self._height - 6)
#         hanimate.setKeyValueAt(0.7, 165)
#         hanimate.setKeyValueAt(0.9, 170)
        hanimate.setKeyValueAt(1, self._height)

        self.animate = QParallelAnimationGroup(self)
        self.animate.addAnimation(wanimate)
        self.animate.addAnimation(hanimate)

    def enterEvent(self, event):
        super(RubberBandButton, self).enterEvent(event)
        self.animate.stop()
        self.animate.start()

    def setWidth(self, width):
        self._width = width

    def getWidth(self):
        return self._width

    def setHeight(self, height):
        self._height = height

    def getHeight(self):
        return self._height

    def getBgColor(self):
        return self._bgcolor

    def setBgColor(self, color):
        self._bgcolor = color

    width = pyqtProperty(int, getWidth, setWidth)
    height = pyqtProperty(int, getHeight, setHeight)
    bgColor = pyqtProperty(str, getBgColor, setBgColor)


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout
    app = QApplication(sys.argv)
    app.setStyleSheet('''
    RubberBandButton {
        min-width: 200px;
        max-width: 200px;
        min-height: 200px;
        max-height: 200px;
        border: none;
        color: white;
        outline: none;
        margin: 4px;
        qproperty-bgColor: #ff0000;
    }
    ''')
    w = QWidget()
    w.resize(800, 600)
    layout = QHBoxLayout(w)
    layout.addWidget(RubberBandButton("hello", w))
    w.show()
    sys.exit(app.exec_())
