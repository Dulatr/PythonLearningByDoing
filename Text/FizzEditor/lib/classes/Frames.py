import wx
import os

class TopFrame(wx.Frame):
    def __init__(self,parent,title):
        
        wx.Frame.__init__(self,parent,title=title,size=(1000,700))

        self.control = wx.TextCtrl(self,style=wx.TE_MULTILINE)
        self.contentNotSaved = True
        self.Show(True)
        
        # Create menus
        fileMenu=wx.Menu()
        newMenu=wx.Menu()

        # Menuitems
        save = fileMenu.Append(wx.ID_SAVE,"&Save","Save to a file")
        fileMenu.AppendSeparator()
        _open = fileMenu.Append(wx.ID_OPEN,"&Open","Open a file for edit")
        fileMenu.AppendSeparator()         
        abt = fileMenu.Append(wx.ID_ABOUT,"&About","Info")
        fileMenu.AppendSeparator()
        ext = fileMenu.Append(wx.ID_EXIT,"&Exit","Close the program")

        new = newMenu.Append(wx.ID_NEW,"&New","Newstuff")

        menuBar=wx.MenuBar()
        menuBar.Append(fileMenu,"&File")
        menuBar.Append(newMenu,"&New")

        # Events
        self.Bind(wx.EVT_MENU,self.onAbout,abt)
        self.Bind(wx.EVT_MENU,self.onExit,ext)
        self.Bind(wx.EVT_MENU,self.onNew,new)
        self.Bind(wx.EVT_MENU,self.onSave,save)
        self.Bind(wx.EVT_MENU,self.onOpen,_open)
        self.Bind(wx.EVT_TEXT,self.onChange,self.control)
        
        self.SetMenuBar(menuBar)
        self.Show(True)

    def onAbout(self,event):
        filePath = os.getcwd() + "/docs/about.txt"
        aboutFile = open(filePath,'r')
        aboutText = aboutFile.read()
        aboutFile.close()
        dlg = wx.MessageDialog(self,aboutText,"About Sample editor",wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

    def onExit(self,event):
        if self.contentNotSaved:
            dlg = wx.MessageBox("Progess has not been saved, do you wish to save before exiting?","Please confirm",wx.ICON_QUESTION | wx.YES_NO,None)
            if dlg == wx.NO:
                return
            else:
                self.onSave(event)

        self.Close()

    def onSave(self,event):
        saveto = wx.FileDialog(self,"Choose where to save the file","",style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)

        saveto.ShowModal()

        dirPath = saveto.GetPath()
        if dirPath == "":
            return

        try:
            with open(dirPath, 'w') as File:
                text=self.control.GetValue()
                File.write(text)
        except IOError:
            wx.LogError("Can't you ding bat")
        saveto.Close()

        self.contentNotSaved = False

    def onOpen(self,event):
        if self.contentNotSaved:
            if wx.MessageBox("Current work not saved, do you wish to continue?","Please confirm",wx.ICON_QUESTION | wx.YES_NO,self) == wx.NO:
                return

        with wx.FileDialog(self, "Open file",style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as dlg:
            if dlg.ShowModal() == wx.ID_CANCEL:
                return

            thepath = dlg.GetPath()

            try:
                with open(thepath,'r') as File:
                    self.control.Clear()
                    self.control.AppendText(File.read())
            except IOError:
                wx.LogError("Can't do it you ding bat")

    def onNew(self,event):
        pass

    def onChange(self,event):
        self.contentNotSaved = True