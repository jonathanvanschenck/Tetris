# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 12:29:40 2019

@author: Jonathan
"""
#%%
import numpy as np
import setupVars
import constructor
import initialize
import transformer
from time import sleep

g = np.array([0,3])
dt= 1
fric = np.array([5.0,0.0])
keybindings = [np.array([-5.0,0.0]),np.array([5.0,0.0]),np.array([0.0,35.0])]
vmax = np.array([10.0,40.0])

def step(canvas):
    gameOver = False
    clearedrows = 0
    objF = canvas.find_withtag("Falling")
#    for o in canvas.find_all():
#        print(canvas.gettags(o))
#        print(canvas.bbox(o))
#    print(objF)
#    print(len(objF))
    if len(objF)==0:
        gameOver = undock(canvas)
    else:
        dropB(canvas,objF)
        ground = grounded(canvas,objF)
        if ground:
            clearedrows = rowFilled(canvas)
    return [gameOver,clearedrows]

def update(canvas,key):
    objF = canvas.find_withtag("Falling")
    if len(objF)>0:
        if key[0]==1:
            moveL(canvas,objF)
        if key[1]==1:
            moveR(canvas,objF)
        if key[2]==1:
            transformer.TransformR(canvas,objF)
            if collisionQ(canvas,objF):
                transformer.TransformL(canvas,objF)
    return [False,0]



def undock(canvas):
    objD = canvas.find_withtag("Dock")
    for blocks in objD:
        canvas.move(blocks,
                    -setupVars.marginP-(6+2)*setupVars.PperB,#dx
                    -setupVars.PperB)#dy
        canvas.dtag(blocks,"Dock")
        canvas.addtag_withtag(tagOrId=blocks,newtag="Falling")
    initialize.genBlock(canvas)
    return collisionQ(canvas, objD)

def dropB(canvas,obj):
    for blocks in obj:
        canvas.move(blocks,0,setupVars.PperB)
def raiseB(canvas,obj):
    for blocks in obj:
        canvas.move(blocks,0,-setupVars.PperB)
        
def moveL(canvas,obj):
    for blocks in obj:
        canvas.move(blocks,-setupVars.PperB,0)
    if collisionQ(canvas,obj):
        for blocks in obj:
            canvas.move(blocks,setupVars.PperB,0)
def moveR(canvas,obj):
    for blocks in obj:
        canvas.move(blocks,setupVars.PperB,0)
    if collisionQ(canvas,obj):
        for blocks in obj:
            canvas.move(blocks,-setupVars.PperB,0)

def rotR(canvas,obj):
    pass
            
def collisionQ(canvas,obj):
    collision = False
    for blocks in obj:
        coords = canvas.bbox(blocks)
        if (coords[2] <= setupVars.marginP + setupVars.PperB \
            or coords[2] > setupVars.marginP+setupVars.stageWP + setupVars.PperB \
            or coords[3] >= setupVars.marginP + setupVars.stageHP + setupVars.PperB):
            #If collision with walls/floor
            collision = True
        for Gblocks in canvas.find_withtag("Grounded"):
            Gcoords = canvas.bbox(Gblocks)
            if coords == Gcoords:
                collision = True
    return collision

def grounded(canvas,obj):
    grounded = False
    for blocks in obj:
        coords = canvas.bbox(blocks)
        if coords[3] >= setupVars.marginP + setupVars.stageHP + setupVars.PperB:
            grounded = True
        for Gblocks in canvas.find_withtag("Grounded"):
            Gcoords = canvas.bbox(Gblocks)
            if coords == Gcoords:
                grounded = True
    if grounded:
        raiseB(canvas,obj)
        for blocks in obj:
            canvas.dtag(blocks,"Falling")
            canvas.addtag_withtag(tagOrId=blocks,newtag="Grounded")
    return grounded

def rowFilled(canvas):
    clearedrows = 0
    for i in range(18):
        rowids = canvas.find_enclosed(setupVars.marginP - 1,#x1
                                      setupVars.marginP + i*setupVars.PperB - 1,#y1
                                      setupVars.marginP + setupVars.stageWP + 1,#x2
                                      setupVars.marginP + (i+1)*setupVars.PperB + 1)#y2
        if len(rowids) == 10:
            clearedrows += 1
            for obj in rowids:
                canvas.delete(obj)
            sleep(0.1)
            aboveids = canvas.find_enclosed(setupVars.marginP - 1,#x1
                                            setupVars.marginP - 1,#y1
                                            setupVars.marginP + setupVars.stageWP + 1,#x2
                                            setupVars.marginP + i*setupVars.PperB + 1)#y2
            for obj in aboveids:
                canvas.move(obj,0,setupVars.PperB)
    return clearedrows
                
                
    