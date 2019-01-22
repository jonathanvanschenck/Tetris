# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 23:19:13 2019

@author: Jonathan
"""

#%%
framerate = 60
framesPerStep = 60
downKeyDiv = 10-1
deadFrames = 9

stageWB = 10#blocks
stageHB = 18#blocks
PperB = 40#Pixels/block edge
stageHP = stageHB*PperB
stageWP = stageWB*PperB

dockWB = 4+2#blocks
dockHB = 2+2
dockHP = dockHB*PperB
dockWP = dockWB*PperB

marginP = 20#pixels

scoreWP = dockWP
scoreHP = stageHP-marginP-dockHP

screenW = marginP+stageWP+marginP+dockWP+marginP
screenH = 2*marginP+stageHP

playerH = 10
playerW = 5
playerix = 200
playeriy = 300
