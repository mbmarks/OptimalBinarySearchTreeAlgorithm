import numpy as np
import pandas as pd
import time

from obst import obst
from randomkeygen import randomkeygen
import filehandler
from bstmaker import makeTree

def runTest(n):

    filehandler.eraseTestData()
    
    i = list()
    while (n >= 10):
        i.insert(0,n)
        n = int(n/10)
    
    for j in i:

        p,q = randomkeygen(j)

        start = time.time_ns()

        e,w,root = obst(p,q,j)

        end = (time.time_ns() - start)

        filehandler.writeTestData(j, end)

        filehandler.exportArrFile(e,'e_' + str(j))
        filehandler.exportArrFile(w,'w_' + str(j))
        filehandler.exportArrFile(root,'root_' + str(j))

        tree = makeTree(root)
        filehandler.exportBST(tree)

def testData():
    p = [0.0,0.15,0.10,0.05,0.10,0.20]
    q = [0.05,0.10,0.05,0.05,0.05,0.10]
    return p,q
