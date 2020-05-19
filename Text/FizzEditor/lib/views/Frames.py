import wx
from lib.model import model

class topView(wx.Frame):
    def __init__(self,parent,title="Main Window"):
        
        wx.Frame.__init__(self,parent,title=title,size=(1000,700))

        self.initMenu()
        self.initContent()
        
        self.Show(True)

    # Menu Objects
    def initMenu(self):
        # Create menus
        fileMenu=wx.Menu()
        newMenu=wx.Menu()

        # Menuitems
        self.save = fileMenu.Append(wx.ID_SAVE,"&Save","Save to a file")
        fileMenu.AppendSeparator()
        self._open = fileMenu.Append(wx.ID_OPEN,"&Open","Open a file for edit")
        fileMenu.AppendSeparator()         
        self.about = fileMenu.Append(wx.ID_ABOUT,"&About","Info")
        fileMenu.AppendSeparator()
        self._exit = fileMenu.Append(wx.ID_EXIT,"&Exit","Close the program")

        self.new = newMenu.Append(wx.ID_NEW,"&New","Newstuff")

        menuBar=wx.MenuBar()
        menuBar.Append(fileMenu,"&File")
        menuBar.Append(newMenu,"&New")
        
        self.SetMenuBar(menuBar)

    # content objects
    def initContent(self):
        self.control = wx.TextCtrl(self,style=wx.TE_MULTILINE)
       
