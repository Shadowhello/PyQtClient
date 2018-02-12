#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2018年2月12日
@author: Irony."[讽刺]
@site: http://alyl.vip, http://orzorz.vip, https://coding.net/u/892768447, https://github.com/892768447
@email: 892768447@qq.com
@file: Libraries.Widgets.FramelessWindow
@description: 
'''
import ctypes.wintypes

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2018 Irony.\"[讽刺]"
__Version__ = "Version 1.0"

HTCLIENT = 1
HTCAPTION = 2    # 标题栏
WM_NCHITTEST = 132
WM_NCCALCSIZE = 131
HTLEFT = 10
HTRIGHT = 11
HTTOP = 12
HTTOPLEFT = 13
HTTOPRIGHT = 14
HTBOTTOM = 15
HTBOTTOMLEFT = 16
HTBOTTOMRIGHT = 17


class FramelessWindow(QWidget):

    MARGIN = 4

    def __init__(self, *args, **kwargs):
        super(FramelessWindow, self).__init__(*args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)

    def GET_Y_LPARAM(self, param):
        return param >> 16

    def GET_X_LPARAM(self, param):
        return param & 0xffff

    def nativeEvent(self, eventType, message):
        if eventType == b"windows_generic_MSG":
            msg = ctypes.wintypes.MSG.from_address(message.__int__())
            if msg.message == WM_NCCALCSIZE:
                return True, 0
            if msg.message == WM_NCHITTEST:
                xPos = self.GET_X_LPARAM(msg.lParam) - self.frameGeometry().x()
                yPos = self.GET_Y_LPARAM(msg.lParam) - self.frameGeometry().y()
                return self._setResult(xPos, yPos)
        return super(FramelessWindow, self).nativeEvent(eventType, message)

    def _setResult(self, xPos, yPos):
        wm = self.width() - self.MARGIN
        hm = self.height() - self.MARGIN
        self._canResize = True
        if xPos <= self.MARGIN and yPos <= self.MARGIN:
            # 左上角
            return True, HTTOPLEFT
        elif wm <= xPos <= self.width() and hm <= yPos <= self.height():
            # 右下角
            return True, HTBOTTOMRIGHT
        elif wm <= xPos and yPos <= self.MARGIN:
            # 右上角
            return True, HTTOPRIGHT
        elif xPos <= self.MARGIN and hm <= yPos:
            # 左下角
            return True, HTBOTTOMLEFT
        elif 0 <= xPos <= self.MARGIN and self.MARGIN <= yPos <= hm:
            # 左边(并且上下各留出self.MARGIN的距离)
            return True, HTLEFT
        elif wm <= xPos <= self.width() and self.MARGIN <= yPos <= hm:
            # 右边(并且上下各留出self.MARGIN的距离)
            return True, HTRIGHT
        elif self.MARGIN <= xPos <= wm and 0 <= yPos <= self.MARGIN:
            # 上面(并且左右各留出self.MARGIN的距离)
            return True, HTTOP
        elif self.MARGIN <= xPos <= wm and hm <= yPos <= self.height():
            # 下面(并且左右各留出self.MARGIN的距离)
            return True, HTBOTTOM
        elif yPos < 36 and xPos < self.width() - 108:
            # 标题栏区域
            return True, HTCAPTION
        return True, HTCLIENT


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = FramelessWindow()
    w.setMinimumSize(400, 400)
    w.resize(800, 600)
    w.show()
    sys.exit(app.exec_())
