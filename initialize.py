import constructor
from random import sample

newBlock = [constructor.Square,constructor.SquiggleL,constructor.SquiggleR,
            constructor.Line,constructor.LL,constructor.LR,constructor.T]
def genBlock(canvas):
    sample(newBlock,1)[0](canvas)
    
def initialize(canvas):
    #Creaete Outlines
    constructor.Outlines(canvas)
    #constructor.LR(canvas)
    genBlock(canvas)