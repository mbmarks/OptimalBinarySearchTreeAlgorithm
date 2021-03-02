from random import randint
from sys import maxsize
import numpy as np

def randomkeygen(n):

    p = np.zeros([n+1])
    q = np.zeros([n+1])

    probs = np.zeros([2*n+1])

    s = 0

    for i in range(2*n+1):
        #prevent overflow on the sum random number is restricted
        j = randint(0,int(maxsize/(2*n+1)))
        probs[i] = j
        s = s + probs[i]

    for i in range(2*n+1):
        #normalize
        probs[i] = probs[i]/s

    for i in range(n):
        p[i+1] = probs[i]

    for i in range(n,2*n+1):
        q[i-n] = probs[i]

    return p,q

    