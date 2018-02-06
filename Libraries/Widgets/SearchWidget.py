#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2018年2月6日
@author: Irony."[讽刺]
@site: http://alyl.vip, http://orzorz.vip, https://coding.net/u/892768447, https://github.com/892768447
@email: 892768447@qq.com
@file: Libraries.Widgets.SearchWidget
@description: 
'''
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLineEdit, QAction


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2018 Irony.\"[讽刺]"
__Version__ = "Version 1.0"


class SearchWidget(QLineEdit):

    def __init__(self, *args, **kwargs):
        super(SearchWidget, self).__init__(*args, **kwargs)


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    app.setStyleSheet(open("../../themes/default/style.qss",
                           "rb").read().decode("utf-8"))
    w = SearchWidget()
    w.addAction(QAction(QIcon("../../tmp/1.jpg"),
                        "search", w), w.TrailingPosition)
    w.setClearButtonEnabled(True)
    w.show()
    sys.exit(app.exec_())
