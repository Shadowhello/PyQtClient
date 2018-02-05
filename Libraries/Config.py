#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2018年2月5日
@author: Irony."[讽刺]
@site: http://alyl.vip, http://orzorz.vip, https://coding.net/u/892768447, https://github.com/892768447
@email: 892768447@qq.com
@file: Libraries.Config
@description: 
'''

__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2018 Irony.\"[讽刺]"
__Version__ = "Version 1.0"
CachePath = "tmp/cache"
StoragePath = "tmp/storage"

client_id = "fb79c2dd6754e3083342"
client_secret = "8c87f8a3a5b4a7450daccc671bb8bb056630451c"

# 登录地址
LoginUrl = "https://github.com/login/oauth/authorize?client_id={0}&scope=user".format(
    client_id)

# 获取token地址
TokenUrl = "https://github.com/login/oauth/access_token?client_id={0}&client_secret={1}&code=".format(
    client_id, client_secret)

# 获取用户信息
UserUrl = "https://api.github.com/user?access_token="
