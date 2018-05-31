
#import 
from appJar import gui
import time
import datetime

#gui init
loggerApp = gui("work Log", "1400x300")



#gui operations section
def press(button):
    if button =="submit task":
        task = loggerApp.getEntry("task: ")
        startTime = time.ctime()
        loggerApp.setEntry("time: ", startTime)
        print("Task:" , task )
        print(startTime)


def press2(button):
    if button =="log":
        endTime = time.ctime()
        startTime = loggerApp.getEntry("time: ")
        a =datetime.datetime.strptime(startTime, "%a %b %d %H:%M:%S %Y")
        b =datetime.datetime.strptime(endTime, "%a %b %d %H:%M:%S %Y")
        c = b-a 
        print(c)
        loggerApp.setEntry("elaspedTime: ", c)


#gui add section
loggerApp.addLabel("title", "Input your task below")
loggerApp.addLabelEntry("task: ")
loggerApp.addButtons(["submit task"], press)
loggerApp.addLabelEntry("time: ")
loggerApp.addButtons(["log"], press2)
loggerApp.addLabelEntry("elaspedTime: ")


#loggerApp.setLabelBg("title","blue") # possibly set color shade if I want it
#gui commit run
loggerApp.setFocus("task: ")
loggerApp.go()

