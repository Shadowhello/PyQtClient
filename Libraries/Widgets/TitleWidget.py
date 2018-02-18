#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2018年2月12日
@author: Irony."[讽刺]
@site: http://alyl.vip, http://orzorz.vip, https://coding.net/u/892768447, https://github.com/892768447
@email: 892768447@qq.com
@file: Libraries.Widgets.TitleWidget
@description: 
'''
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QSpacerItem, QSizePolicy,\
    QPushButton


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2018 Irony.\"[讽刺]"
__Version__ = "Version 1.0"


class TitleWidget(QWidget):

    minimized = pyqtSignal()
    maximized = pyqtSignal()
    normaled = pyqtSignal()
    closed = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(TitleWidget, self).__init__(*args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self._initView()

    def showNormalBtn(self, visible):
        self._maximumButton.setVisible(not visible)
        self._normalButton.setVisible(visible)

    def _initView(self):
        layout = QHBoxLayout(self, spacing=0)
        layout.setContentsMargins(0, 0, 0, 0)
        # 左侧空白拉伸
        layout.addItem(QSpacerItem(
            20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        layout.addWidget(QPushButton(
            "", self, objectName="skinButton"))
        layout.addWidget(QPushButton(
            "", self, objectName="minimumButton", clicked=self.minimized.emit))
        self._maximumButton = QPushButton(
            "", self, objectName="maximumButton", clicked=self.maximized.emit)
        layout.addWidget(self._maximumButton)
        self._normalButton = QPushButton(
            "", self, objectName="normalButton", clicked=self.normaled.emit, visible=False)
        layout.addWidget(self._normalButton)
        layout.addWidget(QPushButton(
            "", self, objectName="closeButton", clicked=self.closed.emit))


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
    w = TitleWidget()
    w.show()
    sys.exit(app.exec_())
