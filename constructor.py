import setupVars

def Player(canvas):
    canvas.create_rectangle(setupVars.playerix,setupVars.playeriy,
                            setupVars.playerix+setupVars.playerW,
                            setupVars.playeriy+setupVars.playerH,
                            tags=('player','physics','vx=0000.000','vy=0000.000',
                                  'contact=False','jump=0,1','all'),
                            fill="green",outline="green")

def Outlines(canvas):
    #Stage Frame
    canvas.create_rectangle(setupVars.marginP,#x1
                            setupVars.marginP,#y1
                            setupVars.marginP+setupVars.stageWP,#x2
                            setupVars.marginP+setupVars.stageHP,#y2
                            tags=('Frame','StageFrame','all'))
    #Dock Frame
    canvas.create_rectangle(2*setupVars.marginP+setupVars.stageWP,#x1
                            setupVars.marginP,#y1
                            2*setupVars.marginP+setupVars.stageWP+setupVars.dockWP,#x2
                            setupVars.marginP+setupVars.dockHP,#y2
                            tags=('Frame','DockFrame','all'))
    

def block(canvas,dx=0,dy=0):
    #Creates block in the dock at master location
    return canvas.create_rectangle(2*setupVars.marginP+setupVars.stageWP+(2+dx)*setupVars.PperB,#x1
                                   setupVars.marginP+(1+dy)*setupVars.PperB,#y1
                                   2*setupVars.marginP+setupVars.stageWP+(3+dx)*setupVars.PperB,#x2
                                   setupVars.marginP+(2+dy)*setupVars.PperB,#y2
                                   tags=('Dock','all'),
                                   outline="white")

def Square(canvas):
    #Create Major square
    b = [block(canvas,0,0),block(canvas,1,0),block(canvas,1,1),block(canvas,0,1)]
    for i in range(4):
        canvas.addtag_withtag(newtag='BlockSquare',tagOrId=b[i])
        canvas.addtag_withtag(newtag='b'+str(i),tagOrId=b[i])
        canvas.addtag_withtag(newtag='state=1',tagOrId=b[i])
        canvas.itemconfigure(b[i],fill="green")
def SquiggleL(canvas):
    #Create Major square
    b = [block(canvas,0,0),block(canvas,1,1),block(canvas,0,1),block(canvas,-1,0)]
    for i in range(4):
        canvas.addtag_withtag(newtag='BlockSquiggleL',tagOrId=b[i])
        canvas.addtag_withtag(newtag='b'+str(i),tagOrId=b[i])
        canvas.addtag_withtag(newtag='state=1',tagOrId=b[i])
        canvas.itemconfigure(b[i],fill="purple")
def SquiggleR(canvas):
    #Create Major square
    b = [block(canvas,0,0),block(canvas,1,0),block(canvas,0,1),block(canvas,-1,1)]
    for i in range(4):
        canvas.addtag_withtag(newtag='BlockSquiggleR',tagOrId=b[i])
        canvas.addtag_withtag(newtag='b'+str(i),tagOrId=b[i])
        canvas.addtag_withtag(newtag='state=1',tagOrId=b[i])
        canvas.itemconfigure(b[i],fill="blue")
def Line(canvas):
    #Create Major square
    b = [block(canvas,0,0),block(canvas,1,0),block(canvas,2,0),block(canvas,-1,0)]
    for i in range(4):
        canvas.addtag_withtag(newtag='BlockLine',tagOrId=b[i])
        canvas.addtag_withtag(newtag='b'+str(i),tagOrId=b[i])
        canvas.addtag_withtag(newtag='state=1',tagOrId=b[i])
        canvas.itemconfigure(b[i],fill="orange")
def LL(canvas):
    #Create Major square
    b = [block(canvas,0,0),block(canvas,1,0),block(canvas,-1,1),block(canvas,-1,0)]
    for i in range(4):
        canvas.addtag_withtag(newtag='BlockLL',tagOrId=b[i])
        canvas.addtag_withtag(newtag='b'+str(i),tagOrId=b[i])
        canvas.addtag_withtag(newtag='state=1',tagOrId=b[i])
        canvas.itemconfigure(b[i],fill="grey")
def LR(canvas):
    #Create Major square
    b = [block(canvas,0,0),block(canvas,1,0),block(canvas,1,1),block(canvas,-1,0)]
    for i in range(4):
        canvas.addtag_withtag(newtag='BlockLR',tagOrId=b[i])
        canvas.addtag_withtag(newtag='b'+str(i),tagOrId=b[i])
        canvas.addtag_withtag(newtag='state=1',tagOrId=b[i])
        canvas.itemconfigure(b[i],fill="red")
def T(canvas):
    #Create Major square
    b = [block(canvas,0,0),block(canvas,1,0),block(canvas,0,1),block(canvas,-1,0)]
    for i in range(4):
        canvas.addtag_withtag(newtag='BlockT',tagOrId=b[i])
        canvas.addtag_withtag(newtag='b'+str(i),tagOrId=b[i])
        canvas.addtag_withtag(newtag='state=1',tagOrId=b[i])
        canvas.itemconfigure(b[i],fill="yellow")