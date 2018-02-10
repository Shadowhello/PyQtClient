#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2018年2月10日
@author: Irony."[讽刺]
@site: http://alyl.vip, http://orzorz.vip, https://coding.net/u/892768447, https://github.com/892768447
@email: 892768447@qq.com
@file: Libraries.Widgets.LinkWidget
@description: 
'''
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSpacerItem, QSizePolicy

from Libraries.Widgets.LinkButton import LinkButton
from Libraries.Widgets.RubberBandButton import RubberBandButton


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2018 Irony.\"[讽刺]"
__Version__ = "Version 1.0"


class LinkWidget(QWidget):

    def __init__(self, *args, **kwargs):
        super(LinkWidget, self).__init__(*args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self._initView()

    def _initView(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(15)
        layout.setContentsMargins(12, 35, 12, 30)
        layout.addWidget(LinkButton(self, objectName="groupButton1"))
        layout.addWidget(LinkButton(self, objectName="groupButton2"))
        layout.addWidget(LinkButton(self, objectName="qqButton"))
        layout.addWidget(LinkButton(self, objectName="weixinButton"))
        layout.addWidget(LinkButton(self, objectName="alipayButton"))
        layout.addItem(QSpacerItem(
            40, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
        layout.addWidget(RubberBandButton(self, objectName="upButton"))


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
    w = LinkWidget()
    w.show()
    sys.exit(app.exec_())
