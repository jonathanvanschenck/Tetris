#%%
from setupVars import PperB as s

LineTransformsR = {1:[[0,0],[-s,s],[-2*s,2*s],[s,-s],2],
                   2:[[0,0],[s,-s],[2*s,-2*s],[-s,s],1]}
LineTransformsL = LineTransformsR
SquiggleRTransformsR = {1:[[ s,0],[0, s],[0,-s],[ s,-2*s],2],
                        2:[[-s,0],[0,-s],[0, s],[-s, 2*s],1]}
SquiggleRTransformsL = SquiggleRTransformsR
SquiggleLTransformsR = {1:[[ s,0],[-s,0],[0,-s],[ 2*s,-s],2],
                        2:[[-s,0],[ s,0],[0, s],[-2*s, s],1]}
SquiggleLTransformsL = SquiggleLTransformsR
TTransformsR = {1:[[0,0],[-s, s],[-s,-s],[ s,-s],2],
                2:[[0,0],[-s,-s],[ s,-s],[ s, s],3],
                3:[[0,0],[ s,-s],[ s, s],[-s, s],4],
                4:[[0,0],[ s, s],[-s, s],[-s,-s],1]}
TTransformsL = {1:[[0,0],[-s,-s],[ s,-s],[ s, s],4],
                2:[[0,0],[ s,-s],[ s, s],[-s, s],1],
                3:[[0,0],[ s, s],[-s, s],[-s,-s],2],
                4:[[0,0],[-s, s],[-s,-s],[ s,-s],3]}
LLTransformsR = {1:[[0,0],[-s, s],[   0,-2*s],[ s,-s],2],
                 2:[[0,0],[-s,-s],[ 2*s,   0],[ s, s],3],
                 3:[[0,0],[ s,-s],[   0, 2*s],[-s, s],4],
                 4:[[0,0],[ s, s],[-2*s,   0],[-s,-s],1]}
LLTransformsL = {1:[[0,0],[-s,-s],[ 2*s,   0],[ s, s],4],
                 2:[[0,0],[ s,-s],[   0, 2*s],[-s, s],1],
                 3:[[0,0],[ s, s],[-2*s,   0],[-s,-s],2],
                 4:[[0,0],[-s, s],[   0,-2*s],[ s,-s],3]}
LRTransformsR = {1:[[0,0],[-s, s],[-2*s,   0],[ s,-s],2],
                 2:[[0,0],[-s,-s],[   0,-2*s],[ s, s],3],
                 3:[[0,0],[ s,-s],[ 2*s,   0],[-s, s],4],
                 4:[[0,0],[ s, s],[   0, 2*s],[-s,-s],1]}
LRTransformsL = {1:[[0,0],[-s,-s],[   0,-2*s],[ s, s],4],
                 2:[[0,0],[ s,-s],[ 2*s,   0],[-s, s],1],
                 3:[[0,0],[ s, s],[   0, 2*s],[-s,-s],2],
                 4:[[0,0],[-s, s],[-2*s,   0],[ s,-s],3]}


def TransformR(canvas,obj):
    btype = getType(canvas.gettags(obj[0]))
    if btype == "Square":
        return None
    elif btype == "Line":
        transforms = LineTransformsR[popState(canvas,obj)]
        setState(canvas,obj,transforms[4])
    elif btype == "SquiggleR":
        transforms = SquiggleRTransformsR[popState(canvas,obj)]
        setState(canvas,obj,transforms[4])
    elif btype == "SquiggleL":
        transforms = SquiggleLTransformsR[popState(canvas,obj)]
        setState(canvas,obj,transforms[4])
    elif btype == "T":
        transforms = TTransformsR[popState(canvas,obj)]
        setState(canvas,obj,transforms[4])
    elif btype == "LL":
        transforms = LLTransformsR[popState(canvas,obj)]
        setState(canvas,obj,transforms[4])
    elif btype == "LR":
        transforms = LRTransformsR[popState(canvas,obj)]
        setState(canvas,obj,transforms[4])
    else:
        return None
    for i in range(4):
        canvas.move(obj[i],transforms[i][0],transforms[i][1])
        #print("moved")
    return None

def TransformL(canvas,obj):
    btype = getType(canvas.gettags(obj[0]))
    if btype == "Square":
        return None
    elif btype == "Line":
        transforms = LineTransformsL[popState(canvas,obj)]
        setState(canvas,obj,transforms[4])
    elif btype == "SquiggleR":
        transforms = SquiggleRTransformsL[popState(canvas,obj)]
        setState(canvas,obj,transforms[4])
    elif btype == "SquiggleL":
        transforms = SquiggleLTransformsL[popState(canvas,obj)]
        setState(canvas,obj,transforms[4])
    elif btype == "T":
        transforms = TTransformsL[popState(canvas,obj)]
        setState(canvas,obj,transforms[4])
    elif btype == "LL":
        transforms = LLTransformsL[popState(canvas,obj)]
        setState(canvas,obj,transforms[4])
    elif btype == "LR":
        transforms = LRTransformsL[popState(canvas,obj)]
        setState(canvas,obj,transforms[4])
    else:
        return None
    for i in range(4):
        canvas.move(obj[i],transforms[i][0],transforms[i][1])
        #print("moved")
    return None
        


def getType(tag):
    return [i for i in tag if "Block" in i][0][5:]

def popState(canvas,obj):
    tag = canvas.gettags(obj[0])
    state = [i for i in tag if "state=" in i][0]
    for blocks in obj:
        canvas.dtag(blocks,state)
    return int(state[6])
def setState(canvas,obj,state):
    for blocks in obj:
        canvas.addtag_withtag(tagOrId=blocks,newtag="state={}".format(state))