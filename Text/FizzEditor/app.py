#!/usr/bin/env python3.8
from lib.views.Frames import topView
from lib.controller import Controller
import wx

if __name__=="__main__":
    app=wx.App(False)
    controller = Controller(app)
    app.MainLoop()