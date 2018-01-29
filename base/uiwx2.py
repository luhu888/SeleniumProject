# __author__=luhu
# -*- coding: utf-8 -*-
import wx

app = wx.App()
window = wx.Frame(None, title=u"API测试", size=(400, 300))
panel = wx.Panel(window)
label = wx.StaticText(panel, label=u"第一个gui程序", pos=(150, 100))
window.Show(True)
app.MainLoop()