#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2018年2月7日
@author: Irony."[讽刺]
@site: http://alyl.vip, http://orzorz.vip, https://coding.net/u/892768447, https://github.com/892768447
@email: 892768447@qq.com
@file: Libraries.Network
@description: 
'''
from PyQt5.QtCore import QObject
from PyQt5.QtNetwork import QNetworkAccessManager


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2018 Irony.\"[讽刺]"
__Version__ = "Version 1.0"


class Network(QNetworkAccessManager):

    _instance = None

    def instance(self, parent: QObject=None)->QNetworkAccessManager:
        if not Network._instance:
            Network._instance = Network(parent)
        return Network._instance

    def __init__(self, *args, **kwargs):
        super(Network, self).__init__(*args, **kwargs)
