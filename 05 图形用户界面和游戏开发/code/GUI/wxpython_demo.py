#!/usr/bin/env python
import wx # pip3 install -U wxPython

# Create a new app
app = wx.App(False)
# A Frame is a top-level window.
frame = wx.Frame(None, wx.ID_ANY, "Hello World")
# Show the frame.
frame.Show(True)
app.MainLoop()
