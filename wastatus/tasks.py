from background_task import background
import time

@background(schedule = 0)
def fun():
    print('BACKGROUND TASK')