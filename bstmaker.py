from binarytree import Node

def populateTree(r,l,h):
    b = int(r[l][h])
    
    root = Node(b)

    if l == h:
        root.left = Node(0)
        root.right = Node(0)
        return root

    if b == l:
        root.left = Node(0)
        root.right = populateTree(r,b+1,h)
        return root

    if b == h:
        root.left = populateTree(r,l,b-1)
        root.right = Node(0)
        return root

    else:
        root.left = populateTree(r,l,b-1)
        root.right = populateTree(r,b+1,h)
        return root

    return root

def pruneTree(root):
    leaves = root.inorder
    count = 0
    for i in range(len(leaves)):
        if leaves[i].value == 0:
            leaves[i].value = count
            count -= 1

def makeTree(r):
    tree = populateTree(r,1,r.shape[0]-1)
    pruneTree(tree)
    return tree