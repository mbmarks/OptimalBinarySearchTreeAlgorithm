import pandas as pd

def exportArrFile(arr,s):
    df = pd.DataFrame(arr)
    df.to_csv('arrays/' + s + '.csv')

def importArrFile(t,s):
    df = pd.read_csv('arrays/' + str(t) + '_' + str(s) + '.csv')
    return df.to_numpy()

def writeTestData(n,ns):
    with open('log/output.log', 'a') as f:
        f.write(str(n) + ' ' + str(ns) + '\n')
    f.close()

def extractTestData():
    tests = list()
    with open('log/output.log', 'r') as f:
        for l in f.readlines():
            tests.append(list(map(int,l.split(' '))))
    f.close()
    return tests

def eraseTestData():
    with open('log/output.log', 'r+') as f:
        f.seek(0)
        f.truncate()
    f.close()

def exportBST(tree):
    with open('img/bst' + str(len(tree.inorder)) + '.txt','w') as f:
        f.write(str(tree))
    f.close

    