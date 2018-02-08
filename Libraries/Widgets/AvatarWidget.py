#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2018年2月8日
@author: Irony."[讽刺]
@site: http://alyl.vip, http://orzorz.vip, https://coding.net/u/892768447, https://github.com/892768447
@email: 892768447@qq.com
@file: Libraries.Widgets.AvatarWidget
@description: 
'''
from PyQt5.QtCore import Qt, QTimer, QPointF, pyqtSignal, pyqtProperty
from PyQt5.QtGui import QPixmap, QPainter, QPainterPath, QColor
from PyQt5.QtWidgets import QWidget, QGraphicsDropShadowEffect, QLabel


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2018 Irony.\"[讽刺]"
__Version__ = "Version 1.0"


class AvatarWidget(QLabel):

    clicked = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(AvatarWidget, self).__init__(*args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self._rotate = 0
        self._radius = 0
        self._step = 45
        self._padding = 10
        self._image = ""
        self._shadowColor = "#212121"
        self._pixmap = None
        self._direction = None    # clockwise 顺时针 anticlockwise 逆时针
        self._timer = QTimer(self, timeout=self.update)
        self._effect = QGraphicsDropShadowEffect(self)
        self._effect.setBlurRadius(self._padding * 2)
        self._effect.setOffset(0, 0)

    def __del__(self):
        del self._pixmap
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
                super(AvatarWidget, self).update()
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
                super(AvatarWidget, self).update()

    def paintEvent(self, event):
        '''绘制事件'''
        if not self._pixmap or self._pixmap.isNull():
            return super(AvatarWidget, self).paintEvent(event)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        ph = self._padding / 2
        if self._direction in ("clockwise", "anticlockwise"):
            painter.translate(self.rect().center())    # 设置中心为旋转的中心
            painter.rotate(self._rotate)  # 旋转
            # 绘制图片
            painter.drawPixmap(
                QPointF((-self.width() + self._padding) / 2, (-self.height() + self._padding) / 2), self._pixmap)
            painter.translate(-self.rect().center())    # 将原点复位
        else:
            painter.drawPixmap(QPointF(ph, ph), self._pixmap)
#         painter.setPen(  # 边框圆圈
#             QPen(QColor(self._shadowColor), 5, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
#         painter.drawRoundedRect(
#             ph, ph, self._pixmap.width(),
#             self._pixmap.height(), self._radius, self._radius)  # 画边框圆圈

    def mouseReleaseEvent(self, event):
        super(AvatarWidget, self).mouseReleaseEvent(event)
        self.clicked.emit()

    def enterEvent(self, event):
        '''鼠标进入事件'''
        self._effect.setColor(QColor(self._shadowColor))
        self._effect.setBlurRadius(self._padding * 2)
        self.setGraphicsEffect(self._effect)
        self._timer.stop()
        self._direction = "clockwise"    # 顺时针旋转
        self._timer.start(20)

    def leaveEvent(self, event):
        '''鼠标离开事件'''
        self._effect.setBlurRadius(0)
        self.setGraphicsEffect(self._effect)
        self._timer.stop()
        self._direction = "anticlockwise"    # 逆时针旋转
        self._timer.start(20)

    def getImage(self)->str:
        return self._image

    def setPixmap(self, path: str)->None:
        self._image = path
        size = min(self.width(), self.height()) - self.padding  # 需要边距的边框
        self._radius = int(size / 2)
        self._pixmap = QPixmap(size, size)
        self._pixmap.fill(Qt.transparent)  # 填充背景为透明
        tmp = QPixmap(path).scaled(
            size, size, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        # QPainter
        painter = QPainter()
        painter.begin(self._pixmap)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setRenderHint(QPainter.SmoothPixmapTransform, True)
        # QPainterPath
        path = QPainterPath()
        path.addRoundedRect(0, 0, size, size, self._radius, self._radius)
        # 切割圆
        painter.setClipPath(path)
        painter.drawPixmap(0, 0, tmp)
        painter.end()
        del tmp

    def getPadding(self)->int:
        return self._padding

    def setPadding(self, padding):
        self._padding = padding

    def getShadowColor(self)->str:
        return self._shadowColor

    def setShadowColor(self, color: str):
        self._shadowColor = color

    image = pyqtProperty(str, getImage, setPixmap)
    padding = pyqtProperty(int, getPadding, setPadding)
    shadowColor = pyqtProperty(str, getShadowColor, setShadowColor)


if __name__ == "__main__":
    import sys
    import os
    os.chdir("../../")
    from PyQt5.QtWidgets import QApplication, QVBoxLayout
    app = QApplication(sys.argv)
    app.setStyleSheet(open("themes/default/style.qss",
                           "rb").read().decode("utf-8"))
    parent = QWidget(objectName="Widget",
                     styleSheet="#Widget{background: white;}")
    layout = QVBoxLayout(parent)
    layout.setContentsMargins(20, 20, 20, 20)
    layout.addWidget(AvatarWidget())
    parent.show()
    sys.exit(app.exec_())
