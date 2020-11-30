from background_task import background
import time

file = open('file.txt','a')
file.close()

@background(schedule = 0)
def fun():
    print('BACKGROUND TASK')