'''
Created on May 1, 2013

@author: sushilthe
'''
import wx
from mainaction import ParentFrame
from dialogaction import DialogFrame

class SimpleGUI(wx.App):
    def OnInit(self):
	Dialog = DialogFrame(None)
        Dialog.ShowModal()
        self.frame = ParentFrame(None)
        self.frame.Show()
        return True
    

if __name__ == "__main__":
    app = SimpleGUI()
    app.MainLoop()
    
