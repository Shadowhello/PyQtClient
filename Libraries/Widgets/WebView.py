#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2018年2月5日
@author: Irony."[讽刺]
@site: http://alyl.vip, http://orzorz.vip, https://coding.net/u/892768447, https://github.com/892768447
@email: 892768447@qq.com
@file: Libraries.Widgets.WebView
@description: 
'''
from random import randint

from PyQt5.QtCore import QUrl, QBuffer, QUrlQuery, pyqtSignal, QTimer, Qt
from PyQt5.QtNetwork import QNetworkCookie
from PyQt5.QtWebEngineCore import QWebEngineUrlSchemeHandler,\
    QWebEngineUrlRequestJob
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile,\
    QWebEngineSettings
from PyQt5.QtWidgets import QWidget

from Libraries import Config


# from PyQt5.QtGui import QPalette
__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2018 Irony.\"[讽刺]"
__Version__ = "Version 1.0"

InjectJs = '''
//document.body.style.background='transparent';
//try{
//    document.getElementsByClassName('create-account-callout')[0].style.background='white';
//}catch(e){}
//添加关闭按钮
//登录页面
var target;
var tabindex = 4;
target = document.getElementsByName('commit')[0];
if(target===undefined) {
    tabindex = 2;
    target = document.getElementsByName('authorize')[0];
}
if(target!==undefined) {
    target = target.parentNode;
    target.innerHTML = target.innerHTML + '<button id="closeWindow" class="btn btn-danger btn-block width-full ws-normal" name="close" tabindex="4" type="button" value="">Close</button>';
    document.getElementById("closeWindow").onclick = function() {
        open("pyqtclient://close", "_self");
    }
}
'''


class UrlSchemeHandler(QWebEngineUrlSchemeHandler):
    '''自定义scheme'''

    codeGeted = pyqtSignal(str)

    def requestStarted(self: QWebEngineUrlSchemeHandler, request: QWebEngineUrlRequestJob) -> None:
        '''
        see: http://doc.qt.io/qt-5/qwebengineurlschemehandler.html#requestStarted
        :param info: see http://doc.qt.io/qt-5/qwebengineurlrequestjob.html
        '''
        # 隐藏浏览器窗口
        self.parent().hide()
        url = request.requestUrl().toString()
        if url.startswith("pyqtclient://close"):
            self._close(request)
            return
        if url.startswith("pyqtclient://login"):
            # 把得到的code返回给其它窗口
            self.codeGeted.emit(
                QUrlQuery(request.requestUrl()).queryItemValue("code"))
            # 关闭窗口(30秒以后，保证cookie被写入,bug)
            QTimer.singleShot(30000, lambda: self._close(request))

    def _close(self, request):
        buffer = QBuffer(self)
        buffer.setData(
            b"<html><head><script>window.close();</script></head></html>")
        request.reply(b"text/html", buffer)
        self.parent().close()


class WebView(QWebEngineView):

    _instance = None
    _cookies = []
    closed = pyqtSignal()
    codeGeted = pyqtSignal(str)

    def instance(self, parent: QWidget=None)->QWebEngineView:
        if not WebView._instance:
            WebView._instance = WebView(parent)
        return WebView._instance

    def __init__(self, *args, **kwargs):
        super(WebView, self).__init__(*args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        profile = self.page().profile()
        # 去掉滚动条,ShowScrollBars=25,为5.10新增
        self.page().settings().setAttribute(QWebEngineSettings.ShowScrollBars, False)
        # 设置缓存以及储存路径
        profile.setCachePath(Config.CachePath)
        profile.setPersistentStoragePath(Config.StoragePath)
        profile.setPersistentCookiesPolicy(
            QWebEngineProfile.ForcePersistentCookies)
        # 清理缓存
        profile.clearHttpCache()
        # 清理浏览记录
        profile.clearAllVisitedLinks()
        # 绑定cookie被添加的信号槽
#         profile.cookieStore().cookieAdded.connect(self.onCookieAdd)
        # 安装自定义的url scheme
        url_handler = UrlSchemeHandler(self)
        url_handler.codeGeted.connect(self.codeGeted.emit)
        profile.installUrlSchemeHandler(b"pyqtclient", url_handler)
        # 绑定page的关闭事件,可以通过window.close()触发
        self.page().windowCloseRequested.connect(self.close)
        # 加载完成事件
        self.loadFinished.connect(self.onLoadFinished)

    def load(self, url: str)->None:
        super(WebView, self).load(QUrl(url))

    def closeEvent(self, event)->None:
        super(WebView, self).closeEvent(event)
        self.closed.emit()

    def clearCookies(self)->None:
        '''
        clear all cookies
        '''
        cookieStore = self.page().profile().cookieStore()
        cookieStore.deleteAllCookies()
        cookieStore.deleteSessionCookies()

    def onCookieAdd(self, cookie: QNetworkCookie)->None:
        self._cookies.append(cookie)

    def onLoadFinished(self, _=None):
        self.page().runJavaScript(InjectJs)

    @classmethod
    def initDevPort(cls):
        while 1:
            port = randint(10000, 65534)
            print("port", port)
            if not os.popen("netstat -an | findstr :" + str(port)).readlines():
                break
        print("dev port:", port)
        os.environ["QTWEBENGINE_REMOTE_DEBUGGING"] = str(port)


class OAuthView(WebView):

    def __init__(self, *args, **kwargs):
        super(OAuthView, self).__init__(*args, **kwargs)
        self.setMaximumSize(500, 860)
        self.setMinimumSize(500, 860)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 去掉边框
        self.setContextMenuPolicy(Qt.NoContextMenu)  # 去掉右键菜单


if __name__ == "__main__":
    import sys
    import os
    from PyQt5.QtWidgets import QApplication
    Config.CachePath = "../../tmp/tmp/cache"
    Config.StoragePath = "../../tmp/tmp/storage"
    app = QApplication(sys.argv)
    OAuthView.initDevPort()
    w = OAuthView()
    w.clearCookies()
    w.show()
    w.load(Config.LoginUrl)
    w.codeGeted.connect(lambda x: print("code:", x))
    sys.exit(app.exec_())
