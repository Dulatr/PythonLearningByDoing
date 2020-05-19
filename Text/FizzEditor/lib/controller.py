from lib.model import model
from lib.views.Frames import topView
import os
import wx

class Controller:
    def __init__(self,app):
        self.model = model()
        self.view = topView(None)
        self.contentNotSaved = True
    
        #controller binds view items to control logic
        self.view.Bind(wx.EVT_MENU,self.save,self.view.save)
        self.view.Bind(wx.EVT_MENU,self._open,self.view._open)
        self.view.Bind(wx.EVT_MENU,self.about,self.view.about)
        self.view.Bind(wx.EVT_MENU,self._exit,self.view._exit)

        #controller binds view controls to control logic
        self.view.Bind(wx.EVT_TEXT,self.onChange,self.view.control)

    # user input to text control, update the model
    def onChange(self,event):
        self.model.updateText(event.GetEventObject().GetValue())
        self.contentNotSaved = True

    def save(self,event):
        saveto = wx.FileDialog(None,"Choose where to save the file","",style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)

        saveto.ShowModal()

        dirPath = saveto.GetPath()
        if dirPath == "":
            return

        try:
            with open(dirPath, 'w') as File:
                text=self.model.getText()
                File.write(text)
        except IOError:
            wx.LogError("Can't you ding bat")
        
        self.contentNotSaved = False
     
    def _open(self,event):
        if self.contentNotSaved:
            if wx.MessageBox("Current work not saved, do you wish to continue?","Please confirm",wx.ICON_QUESTION | wx.YES_NO,None) == wx.NO:
                return

        with wx.FileDialog(None, "Open file",style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as dlg:
            if dlg.ShowModal() == wx.ID_CANCEL:
                return

            thepath = dlg.GetPath()

            try:
                with open(thepath,'r') as File:
                    self.model.updateText(File.read())
                self.view.control.AppendText(self.model.textData)
            except IOError:
                wx.LogError("Can't do it you ding bat")
        
        self.contentNotSaved = False

    def new(self,event):
        pass
    
    def about(self,event):
        filePath = os.getcwd() + "/docs/about.txt"
        
        with open(filePath) as aboutFile:
            aboutText = aboutFile.read()
    
        dlg = wx.MessageDialog(None,aboutText,"About Sample editor",wx.OK)
        dlg.ShowModal()

    def _exit(self,event):
        if self.contentNotSaved:
            if wx.MessageBox("Current work not saved, do you wish to continue?","Please confirm",wx.ICON_QUESTION | wx.YES_NO,None) == wx.YES:
                self.save(None)
            else: 
                return
        self.view.Close()            

