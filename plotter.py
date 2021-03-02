import matplotlib.pyplot as plt
import numpy as np

from filehandler import extractTestData

def makePlot():
    l = extractTestData()

    x = list()
    y = list()
    #y for Big Theta Θ comparison
    y2 = list()


    for i in l:
        if i[0] not in x:
            x.append(i[0])
            y.append(i[1])

    for i in x:
        y2.append(i*i*i)

    x = np.array(x)
    y = np.array(y)
    y2 = np.array(y2)

    plt.plot(x,y,marker='.',label='OBST')
    plt.plot(x,y2,marker='o',label='Θ(n^3)')
    plt.xscale('log')
    plt.yscale('log')
    plt.ylabel('Time (ns)')
    plt.xlabel('# of Keys')
    plt.title('OBST Sort Times')
    plt.legend()

    plt.savefig('img/plot.png')