import time
import datetime


#testing the time script
#alrighty lets figure this thing out

ti = time.time()
print(ti)

ti1 = time.time()
ti2 = ti1- ti
print(ti2)



a =datetime.datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y")
print(a)
