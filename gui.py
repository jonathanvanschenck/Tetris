# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 12:30:30 2019

@author: Jonathan
"""
#%%
import tkinter as tk
#import matplotlib.pyplot as plt
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg as FigCan

import engine
import setupVars
import initialize
#%%
class App(tk.Frame):
    keyList = {"a":0, "d":1, "w":2, "s":3}
    
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.grid(row=0)
        self.createWidgets(master)
        self.setupBindings(master)
        
    def createWidgets(self,master):
        #create Start/stop Buttons
        self.buttonFrame = tk.LabelFrame(master)
        self.buttonFrame.grid(row=0,column=0)
        self.startB = tk.Button(self.buttonFrame,text="Start",command=self.startGame)
        self.startB.grid(row=0,column=0)
        self.stopB = tk.Button(self.buttonFrame,text="Stop",command=self.stopGame)
        self.stopB.configure(state="disabled")
        self.stopB.grid(row=0,column=1)
        self.pauseB = tk.Button(self.buttonFrame,text="Pause",command=self.pauseGame)
        self.pauseB.configure(state="disabled")
        self.pauseB.grid(row=0,column=2)
        self.gameRunning=False
        self.currentFrameIndex = 0
        self.currentFrameLabel = tk.Label(self.buttonFrame,text="Frame: {}".format(self.currentFrameIndex))
        self.currentFrameLabel.grid(row=0,column=3)
        #Create Game Space
        self.canvasFrame = tk.LabelFrame(master,text="Game Region")
        self.canvasFrame.grid(row=1,column=0)
        self.canvas = tk.Canvas(self.canvasFrame,width=setupVars.screenW,
                                height=setupVars.screenH)
        self.canvas.grid(row=0,column=0)        
        #Create Terminal
        self.term = tk.Text(master,height=4)
        self.term.grid(row=2,column=0)
        
    def setupBindings(self,master):
        #Look for key presses
        self.key = [0,0,0,0]
        self.master.bind("<Key>",self.keyPress)
        self.master.bind("<KeyRelease>",self.keyRelease)
        #Look for clicks in window
        self.canvas.bind("<Button-1>", self.lclick)
    
    def lclick(self,event):
        self.printTerm("Clicked at: x={0:.0f}, y={1:.0f}".format(event.x,event.y))
        
    def keyPress(self,event):
        key = repr(event.char).strip("\'")
        if key in self.keyList and self.gameRunning:
            self.key[self.keyList[key]] = 1
            self.printTerm("Pressed: {} key".format(key))
        else:
            pass
    def keyRelease(self,event):
        key = repr(event.char).strip("\'")
        if key in self.keyList and self.gameRunning:
            self.key[self.keyList[key]] = 0
            self.printTerm("Released: {} key".format(key))
        else:
            pass
        
    def printTerm(self,message):
        self.term.insert(tk.END,"\n\r"+message)
        self.term.see(tk.END)

    def startGame(self):
        self.stopB.configure(state="normal")
        self.pauseB.configure(state="normal")
        self.startB.configure(state="disabled")
        self.gameRunning = True
        self.gameOver = False
        self.gameWin = False
        initialize.initialize(self.canvas)
        #self.player = self.canvas.create_rectangle(100,100,200,200)
        #self.canvas.addtag_closest("player",100,100)
        #self.master.bind("<Key>",self.keyPress)
        self.currentFrameIndex = 1
        self.currentFrameLabel.configure(text="Frame: {}".format(self.currentFrameIndex))
        self.key = [0,0,0,0]
        self.updateGame()
        
    def updateGame(self):
        if self.gameRunning and not self.gameOver and not self.gameWin:
            if (self.currentFrameIndex % (setupVars.framesPerStep//(self.key[3]*setupVars.downKeyDiv+1))) == 0:
                result = engine.step(self.canvas)
            else:
                result = engine.update(self.canvas,self.key)
            self.gameOver = result[0]
#            self.gameWin = result[1]
            self.currentFrameIndex += 1
            self.currentFrameLabel.configure(text="Frame: {}".format(self.currentFrameIndex))
            self.after(int(1000/setupVars.framerate),self.updateGame)
        elif self.gameRunning and (self.gameOver or self.gameWin):
            self.gameRunning = False
            self.printTerm(engine.np.array(["Game Over!","Game Win!"])[[self.gameOver,self.gameWin]][0])
            self.after(int(1000/setupVars.framerate),self.updateGame)
        else:
            pass
    
    def pauseGame(self):
        self.gameRunning = (not self.gameRunning) and (not self.gameOver)
        self.updateGame()
        
    def stopGame(self):
        self.startB.configure(state="normal")
        self.stopB.configure(state="disabled")
        self.pauseB.configure(state="disabled")
        self.canvas.delete("all")
        self.gameRunning = False
        #self.master.bind("<Key>",lambda event: pass)


class gameObject:
    pass
#%%
    
if __name__ == "__main__":
    app = App()
    app.master.title("Game Test")
    app.mainloop()
