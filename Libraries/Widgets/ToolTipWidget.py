#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2018年2月14日
@author: Irony."[讽刺]
@site: http://alyl.vip, http://orzorz.vip, https://coding.net/u/892768447, https://github.com/892768447
@email: 892768447@qq.com
@file: Libraries.Widgets.ToolTipWidget
@description: 
'''
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QPushButton, QWidget


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2018 Irony.\"[讽刺]"
__Version__ = "Version 1.0"


class ToolTipWidget(QLabel):

    _instance = None

    @classmethod
    def instance(cls, parent: QWidget=None)->QLabel:
        if not ToolTipWidget._instance:
            ToolTipWidget._instance = ToolTipWidget(parent)
            ToolTipWidget._instance.setParent(parent)
        return ToolTipWidget._instance

    def __init__(self, *args, **kwargs):
        super(ToolTipWidget, self).__init__(*args, **kwargs)
        self.setVisible(False)
        self.setAlignment(Qt.AlignCenter)
        self._pixmaps = {}

    def __del__(self):
        self._pixmaps.clear()

    def show(self, geometry, text=""):
        self.setContentsMargins(0, 0, 0, 0)
        self.setText(text)
        self.adjustSize()
        self.setGeometry(
            geometry.x() + geometry.width() + 30,
            geometry.y(),
            self.width() + 30,
            geometry.height()
        )
        self.setVisible(True)
        super(ToolTipWidget, self).show()

    def showImage(self, geometry, image):
        self.setContentsMargins(2, 2, 2, 2)
        self.setText("")
        if image not in self._pixmaps:
            self._pixmaps[image] = QPixmap(image)
        self.setPixmap(self._pixmaps.get(image))  # 取出缓存的pixmap
        self.setScaledContents(True)  # 内容自适应
        self.adjustSize()
        self.setGeometry(
            geometry.x() + geometry.width() + 30,
            geometry.y(),
            self.width() + 30,
            self.height()
        )
        self.setVisible(True)
        super(ToolTipWidget, self).show()

    def hide(self):
        self.setVisible(False)
        super(ToolTipWidget, self).hide()


if __name__ == "__main__":
    import sys
    import os
    os.chdir("../../")
    from PyQt5.QtCore import QEvent
    from PyQt5.QtWidgets import QApplication, QVBoxLayout
    app = QApplication(sys.argv)
    app.setStyleSheet(open("themes/default/style.qss",
                           "rb").read().decode("utf-8"))
    window = QWidget()
    toolTip = ToolTipWidget(window)
    layout = QVBoxLayout(window)

    def eventFilter(obj, event):
        if event.type() == QEvent.ToolTip:
            return True
        if event.type() == QEvent.Enter:
            toolTip.show(obj.geometry(), obj.toolTip())
        elif event.type() == QEvent.Leave:
            toolTip.hide()
        return False

    btn = QPushButton("鼠标放在这上面", window, maximumWidth=100, toolTip="PyQt5")
    layout.addWidget(btn)
    window.show()
    # 事件过滤器
    btn.eventFilter = eventFilter
    btn.installEventFilter(btn)
    sys.exit(app.exec_())
