from Tkinter import *
import ttk
class Application(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        
        self.parent = parent
        
        self.initUI()
        
    def initUI(self):
        self.parent.title("Anyfin Calculator")

        self.mainFrame = ttk.Frame(self, relief=RAISED, borderwidth=1)
        self.mainFrame.grid(column=0, row=0)
        
        self.EBLabel = ttk.Label(self.mainFrame, justify=LEFT, text="Enemy Board: ")
        self.EBLabel.grid(column=0, row=0)
        
        self.ebContents = StringVar()
        self.EBContent = ttk.Label(self.mainFrame, textvariable=self.ebContents)
        self.EBContent.grid(column=1, row=0)
        self.ebContents.set("_ _ _ _ _ _ _")

        self.YBLabel = ttk.Label(self.mainFrame, justify=LEFT, text="Your Board: ")
        self.YBLabel.grid(column=0, row=1)
        
        self.ybContents = StringVar()
        self.YBContent = ttk.Label(self.mainFrame, textvariable=self.ybContents)
        self.YBContent.grid(column=1, row=1)
        self.ybContents.set("_ _ _ _ _ _ _")




        dmgFrame = ttk.Frame(self.mainFrame, relief=SUNKEN, borderwidth=5)
        dmgFrame.grid(column=0, row=1)
        
        
        
        
        
        self.grid()
        
        self.placeButtons()
        
        
    def placeButtons(self):
        closeButton = ttk.Button(self, text="Close")
        closeButton.grid(column=1, row=1)
        okButton = ttk.Button(self, text="OK")
        okButton.grid(column=2, row=1)
        
        
    def centerWindow(self):
        width = 400
        height = 400
        screenW = self.parent.winfo_screenwidth()
        screenH = self.parent.winfo_screenheight()
        
        x = (screenW - width)/2
        y = (screenH - height)/2
        
        self.parent.geometry('%dx%d+%d+%d' % (width, height, x, y))
        
def main():
    root = Tk()
    app = Application(root)
    root.mainloop()
    
if __name__ == '__main__':
    main()
