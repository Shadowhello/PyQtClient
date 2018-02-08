#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2018年2月6日
@author: Irony."[讽刺]
@site: http://alyl.vip, http://orzorz.vip, https://coding.net/u/892768447, https://github.com/892768447
@email: 892768447@qq.com
@file: Libraries.Widgets.ContentWidget
@description: 
'''
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2018 Irony.\"[讽刺]"
__Version__ = "Version 1.0"


class ContentWidget(QWidget):

    def __init__(self, *args, **kwargs):
        super(ContentWidget, self).__init__(*args, **kwargs)
        # 保证qss有效
        self.setAttribute(Qt.WA_StyledBackground, True)


if __name__ == "__main__":
    import sys
    import os
    os.chdir("../../")
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    app.setStyleSheet(open("themes/default/style.qss",
                           "rb").read().decode("utf-8"))
    w = ContentWidget()
    w.resize(800, 600)
    w.show()
    sys.exit(app.exec_())
