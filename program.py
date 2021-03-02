import plotter
import tester
import userinterface

while(True):

    userinterface.startmessage()

    i = input()

    if(i == '1'):
        userinterface.runningmessage()
        userinterface.option1()
        i = int(input())
        tester.runTest(i)
        plotter.makePlot()
        userinterface.finishedmessage()
        print()
        break
    
    if(i == '2'):
        userinterface.option2()
        userinterface.runningmessage()
        plotter.makePlot()
        userinterface.finishedmessage()
        print()
        break

    
    if(i == '3'):
        userinterface.quitmessage()
        print()
        break
