#Import needed tools
from GUI import Frame
import wx

#Create the GUI
if __name__ == "__main__":

    app = wx.App()
    frm = Frame(None, title = "Youtube comment sentiment analysis")
    frm.Show()
    app.MainLoop()
