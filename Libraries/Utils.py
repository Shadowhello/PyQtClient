#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2018年2月7日
@author: Irony."[讽刺]
@site: http://alyl.vip, http://orzorz.vip, https://coding.net/u/892768447, https://github.com/892768447
@email: 892768447@qq.com
@file: Libraries.Utils
@description: 
'''
import logging
import os

from PyQt5.QtGui import QFontDatabase

from Libraries.Settings import Settings


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2018 Irony.\"[讽刺]"
__Version__ = "Version 1.0"

LogName = "PyQtClient"


def initLogging(name="PyQtClient", path="tmp", level=logging.DEBUG):
    '''日志'''
    fHandler = logging.FileHandler(os.path.join(path, "log.log"), mode="w")
    formatter = logging.Formatter(
        "[%(asctime)s %(name)s:%(lineno)s] %(levelname)-8s %(message)s"
        if level == logging.DEBUG else "[%(asctime)s %(name)s] %(levelname)-8s %(message)s")
    fHandler.setFormatter(formatter)
    sHandler = logging.StreamHandler()
    sHandler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.addHandler(fHandler)
    logger.addHandler(sHandler)
    logger.setLevel(level)


def loadFont():
    '''加载外部字体'''
    path = Settings.instance("config.ini").font
    if os.path.isfile(path):
        QFontDatabase.addApplicationFont(path)
    else:
        logging.getLogger(LogName).warning("{0} not found".format(path))


def loadStyle(theme="default", encoding="utf-8"):
    '''加载主题样式'''
    Settings.instance("config.ini").theme = theme
    path = Settings.instance("config.ini").style
    if not os.path.isfile(path):
        logging.getLogger(LogName).warning("{0} not found".format(path))
        return ""
    try:
        return open(path, "rb").read().decode(encoding)
    except Exception as e:
        logging.getLogger(LogName).warning(str(e))
