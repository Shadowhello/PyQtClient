#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2018年2月18日
@author: Irony."[讽刺]
@site: http://alyl.vip, http://orzorz.vip, https://coding.net/u/892768447, https://github.com/892768447
@email: 892768447@qq.com
@file: Libraries.Widgets.SkinWidget
@description: 
'''
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGridLayout, QScrollArea, QWidget, QVBoxLayout, QLabel,\
    QSpacerItem, QSizePolicy

from Libraries.Widgets.TitleWidget import TitleWidget
from Libraries.Widgets.FramelessWindow import FramelessWindow


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2018 Irony.\"[讽刺]"
__Version__ = "Version 1.0"


class ThemeItem(QWidget):

    def __init__(self, file, *args, **kwargs):
        super(ThemeItem, self).__init__(*args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setCursor(Qt.PointingHandCursor)
        name = os.path.basename(os.path.dirname(file))
        self.setToolTip(name)
        layout = QVBoxLayout(self, spacing=5)
        layout.setContentsMargins(0, 0, 0, 0)
        self.imageLabel = QLabel(self, objectName="imageLabel")
        layout.addWidget(self.imageLabel)
        layout.addWidget(QLabel(name, self))
        self.image_path = os.path.join("themes", name, "preview.png")

    def resizeEvent(self, event):
        # 当控件的大小变动时才设置缩放后的图片
        if os.path.isfile(self.image_path):
            self.imageLabel.setPixmap(
                QPixmap(self.image_path).scaled(self.imageLabel.size()))
        super(ThemeItem, self).resizeEvent(event)

    def mouseReleaseEvent(self, event):
        print(event)
        super(ThemeItem, self).mouseReleaseEvent(event)


class GridWidget(QWidget):

    def __init__(self, *args, **kwargs):
        super(GridWidget, self).__init__(*args, **kwargs)
        self._layout = QGridLayout(self, spacing=10)
        self._layout.setContentsMargins(10, 10, 10, 10)

    def init(self, path):
        style_files = []
        for name in os.listdir(path):
            tpath = os.path.join(path, name)
            spath = os.path.join(tpath, "style.qss")
            if not os.path.isdir(tpath) or not os.path.isfile(spath):
                continue
            style_files.append(spath)
        style_files = self.splist(style_files, 5)
        for row, items in enumerate(style_files):
            for col, file in enumerate(items):
                self._layout.addWidget(ThemeItem(file, self), row, col)
        length = len(style_files)
        if length == 0:
            return
        # 在第一行最后添加伸展条
        self._layout.addItem(QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum), 0, len(style_files[0]))
        # 在第一列最后添加伸展条
        self._layout.addItem(QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding), length, 0)

    def splist(self, src, length):
        # 等分列表
        return [src[i:i + length] for i in range(len(src)) if i % length == 0]


class SkinWidget(FramelessWindow):
    
    TITLE_WIDTH = 36

    def __init__(self, *args, **kwargs):
        super(SkinWidget, self).__init__(*args, **kwargs)
        self.resize(800, 700)
        layout = QVBoxLayout(self, spacing=0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(TitleWidget(True, True, False, False,
                                     False, False, True, parent=self))
        scrollWidget = QScrollArea(self)
        layout.addWidget(scrollWidget)

        scrollWidget.setFrameShape(QScrollArea.NoFrame)
        scrollWidget.setWidgetResizable(True)
        scrollWidget.setAlignment(Qt.AlignCenter)
        # 网格窗口
        self._widget = GridWidget(scrollWidget)
        scrollWidget.setWidget(self._widget)
        self._widget.init("themes")


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
    w = SkinWidget()
    w.show()
    sys.exit(app.exec_())
