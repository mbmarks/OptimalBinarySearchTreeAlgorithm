import numpy as np


def obst(p,q,n):
    """OBST Optimal Binary Search Tree
    Takes in a size of two probabilites and returns two 2D arrays
    that map the optimal binary search tree

    p - key probabilites
    q - dummy probabilites
    n - number of keys
    """
    e = np.zeros((n+2,n+1))
    w = np.zeros((n+2,n+1))
    root = np.zeros((n+1,n+1))

    for i in range(1,n+2):
        e[i,i-1] = q[i-1]
        w[i,i-1] = q[i-1]
    for l in range(1,n+1):
        for i in range(1,n-l+2):
            j = i + l - 1
            e[i,j] = float('inf')
            w[i,j] = w[i,j-1] + p[j] + q[j]
            for r in range(i, j+1):
                t = e[i,r-1] + e[r+1,j] + w[i,j]
                print(f'Checking array {n} at {r} at [{i},{j}]')
                if (t < e[i,j]):
                    e[i,j] = t
                    root[i,j] = r

    return e, w, root
