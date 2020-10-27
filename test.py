import time
import math


def intunoplus(arg):
    start = time.perf_counter()
    for i in range(arg):
        +i
    restime = time.perf_counter() - start #- intemptycycle(arg)
    opers = arg / restime
    return(opers , restime)

def intemptycycle(arg):
    start = time.perf_counter()
    for i in range(arg):
        i
    restime = time.perf_counter()- start
    opers = arg / restime
    return(restime)


arg = 30000000
print(intunoplus(arg))
print(intemptycycle(arg))
