import tkinter as tk
class GameMenu(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, master= parent)
        self.scale = 0
        self.hardship = 0
        self.configure(background="#E6E6FA")
        # --------------------- Set Game Scale ---------------------
        # Scale Label
        tk.Label(self, text="---- Set Game Scale ----", background="#E6E6FA", font= ("sans-serif",14)).pack()
        # Scale Frame
        self.scalesframe = tk.Frame(self, background= "#E6E6FA")
        self.scalesframe.pack(fill=tk.BOTH, expand=tk.YES)
        rbtn_var = tk.IntVar()
        # Scale
        self.selectedscale = 10
        # Scale 10
        self.scale10 = tk.Radiobutton(self.scalesframe, text = "Scale 10", background= "#E6E6FA", font= ("sans-serif",10), variable= rbtn_var, value= 10 , command= lambda: enterscale(self.scale10) )
        self.scale10.pack(fill= tk.X, side= tk.LEFT, expand= tk.YES)
        # Scale 15
        self.scale15 = tk.Radiobutton(self.scalesframe, text = "Scale 15", background= "#E6E6FA", font= ("sans-serif",10), variable= rbtn_var, value= 15, command= lambda:  enterscale(self.scale15) )
        self.scale15.pack(fill= tk.X, side= tk.RIGHT, expand= tk.YES)
        def enterscale(setscale): self.selectedscale = setscale.cget("value")
        # --------------------- Set Game Hardship ---------------------
        # Hardship Label
        tk.Label(self, text="---- Set Game Hardship ----", background= "#E6E6FA", font= ("sans-serif",14)).pack()
        # Hardship Frame
        self.hardshipframe = tk.Frame(self, background= "#E6E6FA")
        self.hardshipframe.pack(fill=tk.BOTH, expand=tk.YES)
        hp = tk.IntVar()
        # Hardship
        self.sethardship = 0.3
        # Easy
        self.easy = tk.Radiobutton(self.hardshipframe, text = " Easy", background= "#E6E6FA", font= ("sans-serif",10), variable= hp, value= 3, command= lambda: setHardship() )
        self.easy.pack(fill= tk.X, side= tk.LEFT, expand= tk.YES)
        # Medium
        self.medium = tk.Radiobutton(self.hardshipframe, text = " Medium", background= "#E6E6FA", font= ("sans-serif",10), variable= hp, value= 4, command= lambda: setHardship())
        self.medium.pack(fill= tk.X, side= tk.LEFT, expand= tk.YES)
        # Hard
        self.hard = tk.Radiobutton(self.hardshipframe, text = " Hard", background= "#E6E6FA", font= ("sans-serif",10), variable= hp, value= 5, command= lambda: setHardship())
        self.hard.pack(fill= tk.X, side= tk.LEFT, expand= tk.YES)
        def setHardship(): self.sethardship = hp.get()/10
        # --------------------- Show False Btn (Make More Easy) ---------------------
        tk.Label(self,text="---- Make More Easy ----", background= "#E6E6FA",font= ("sans-serif",14)).pack()
        self.showfalsebtns = False
        cbt_var = tk.BooleanVar()
        self.falesbtns = tk.Checkbutton(self, text= "Show Some 'False' Buttons", background= "#E6E6FA", variable= cbt_var, onvalue= True, offvalue= False, command= lambda: checkShowFalseBtns(), font= ("sans-serif",14))
        def checkShowFalseBtns(): self.showfalsebtns = cbt_var.get()
        self.falesbtns.pack(fill= tk.BOTH, expand= tk.YES)
        # --------------------- Start Button ---------------------
        tk.Label(self,text="---------------------------", background= "#E6E6FA", font= ("sans-serif",14)).pack()
        self.startbutton = tk.Button(self, text="Start", background="#7393B3", font= ("sans-serif",20))
        self.startbutton.pack(pady=10)