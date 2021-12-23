import tkinter as tk
from gameConfig.gameMenu import GameMenu
from gameConfig.gamePad import GamePad
class StartGame(GameMenu, GamePad):
    location = "Menu"
    def __init__(self):
        if StartGame.location == "Menu":
            GameMenu.__init__(self, parent= root)
            self.startbutton.configure(command= lambda: self.startbtn())
            self.pack()
        elif StartGame.location == "GamePad":
            GamePad.__init__(self, parent= root, gameScale= self.selectedscale, gamehardship= self.sethardship, showsomenonepoints= self.showfalsebtns)
            self.menubtn.configure(command= lambda: self.menu())
            self.restartbtn.configure(command= lambda: self.restart())
            self.pack()
    def menu(self):
        self.destroy()
        StartGame.location = "Menu"
        self.__init__()
    def startbtn(self):
        self.destroy()
        StartGame.location = "GamePad"
        self.__init__()
    def restart(self):
        self.destroy()
        self.__init__()
if __name__ == "__main__":        
    root = tk.Tk()
    root.resizable(0, 0)
    start = StartGame()
    start.pack()
    root.mainloop()