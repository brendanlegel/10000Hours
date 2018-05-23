
# coding: utf-8

# In[59]:


"""
In this project I will be creating a script that tells the user how
much time will be needed of programming each day in order to accomplish 10000 hours
In this endeavor I will be using multiple imports ' probably* '
"""


# In[73]:


def HoursAvailable(days, sleep=8, food=2, fun=2):
    #Assuming 24 hours in the day
    wakeTime = (24  
                -sleep
                -food
                -fun
    )
    totalTime = days * wakeTime
    return totalTime


def expertChecker(x):
    if (x > 10000):
        return 1
    else:
        return 0
    
def timeNeeded(sleep,food,fun):
    expert = 0 
    days = 0
    while expert is not 1:
        days += 1 
        expert = expertChecker(HoursAvailable(days,sleep,food,fun))
    return days

def yearMe(days):
    time = int(days/(365)) 
    return time
    
def ageMe(current, new):
    return current + new, new


# In[79]:


def wrapRun():
    print(" please input the following data as a number integer not string")
    yourAge = int(input("whats your age? : "))
    avgSleep= int(input("how much sleep do you average a day?: "))
    avgFood = int(input("how much time do you spend eating a day?: "))
    avgFun = int(input("how much time do you spend on other  activities a day?: "))
    newAge, addedAge = ageMe(yourAge,yearMe(timeNeeded(avgSleep,avgFood,avgFun)))
    print("For you to achieve 10,000 hours in this task it will take you", 
          addedAge, "years, This will make you", 
          newAge,
          "years old in the end")
    if addedAge == 1:
        phrase = str(addedAge) + " year of time for 10000 hours"
    else:
        phrase = str(addedAge) + " years of time for 10000 hours"
    return(phrase)


# In[78]:


wrapRun()


# In[63]:


# well now we know I'll be 24 before I accomplish this task... But thats the goal

