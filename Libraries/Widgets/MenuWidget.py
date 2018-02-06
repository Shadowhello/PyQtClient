#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2018年2月6日
@author: Irony."[讽刺]
@site: http://alyl.vip, http://orzorz.vip, https://coding.net/u/892768447, https://github.com/892768447
@email: 892768447@qq.com
@file: Libraries.Widgets.MenuWidget
@description: 
'''
from PyQt5.QtWidgets import QWidget, QGridLayout, QSpacerItem, QSizePolicy,\
    QLabel, QLineEdit, QTreeWidget


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2018 Irony.\"[讽刺]"
__Version__ = "Version 1.0"


class MenuWidget(QWidget):

    def __init__(self, *args, **kwargs):
        super(MenuWidget, self).__init__(*args, **kwargs)
        # 初始化布局和控件
        self._initView()

    def _initView(self):
        layout = QGridLayout(self)
        layout.setContentsMargins(20, 30, 20, 30)
        layout.setHorizontalSpacing(0)
        layout.setVerticalSpacing(20)
        item = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        # 头像
        layout.addItem(item, 0, 0)
        layout.addWidget(QLabel("dff", self), 0, 1)
        layout.addItem(item, 0, 2)
        # 搜索框
        layout.addItem(item, 1, 0)
        layout.addWidget(QLineEdit(self), 1, 1)
        layout.addItem(item, 1, 2)
        # 例子目录
        layout.addItem(item, 2, 0)
        layout.addWidget(QTreeWidget(self), 2, 1)
        layout.addItem(item, 2, 2)
        #
        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 1)
        layout.setRowStretch(2, 4)


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    app.setStyleSheet(open("../../themes/default/style.qss",
                           "rb").read().decode("utf-8"))
    w = MenuWidget()
    w.resize(800, 600)
    w.show()
    sys.exit(app.exec_())
