#!/usr/bin/env python3.8
from lib.classes.Frames import TopFrame
import wx

if __name__=="__main__":
    app=wx.App(False)
    frame=TopFrame(None,'FizzEditor')
    app.MainLoop()