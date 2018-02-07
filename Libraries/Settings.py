#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2018年2月7日
@author: Irony."[讽刺]
@site: http://alyl.vip, http://orzorz.vip, https://coding.net/u/892768447, https://github.com/892768447
@email: 892768447@qq.com
@file: Libraries.Settings
@description: 
'''
import os

from PyQt5.QtCore import QSettings, QObject, QTextCodec, QByteArray
from PyQt5.QtWidgets import QWidget


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2018 Irony.\"[讽刺]"
__Version__ = "Version 1.0"


class Settings(QSettings):

    _instance = None

    def instance(self, name: str="", parent: QObject=None)->QSettings:
        if not Settings._instance:
            Settings._instance = Settings(name, parent)
        return Settings._instance

    def __init__(self, *args, **kwargs):
        super(Settings, self).__init__(*args, **kwargs)
        self.setDefaultFormat(self.IniFormat)
        self.setIniCodec(QTextCodec.codecForName("utf-8"))

    @property
    def theme(self)->str:
        '''主题'''
        return self.value("theme", "default")

    @theme.setter
    def theme(self, value: str)->None:
        '''
        #设置主题
        :param value: str
        '''
        self.setValue("theme", value)
        self.sync()

    @property
    def font(self)->str:
        '''字体'''
        return os.path.join("themes", self.theme, "font.ttf")

    @property
    def style(self)->str:
        '''主题'''
        return os.path.join("themes", self.theme, "style.qss")

    @property
    def geometry(self):
        '''窗口大小和位置'''
        return self.value("geometry", None, QByteArray)

    @geometry.setter
    def geometry(self, window: QWidget):
        '''保存窗口大小和位置'''
        self.setValue("geometry", window.geometry())
        self.sync()
