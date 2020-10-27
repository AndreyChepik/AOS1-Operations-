import time
import math


def intunoplus(arg):
    start = time.perf_counter()
    for i in range(arg):
        i = +i
    restime = time.perf_counter() - start - intemptycycle(arg)
    opers = math.floor(arg / restime)
    return(opers)

def intunominus(arg):
    start = time.perf_counter()
    for i in range(arg):
        i = -i
    restime = time.perf_counter() - start - intemptycycle(arg)
    opers = math.floor(arg/restime)
    return(opers)


def intplus(arg):
    start = time.perf_counter()
    for i in range(arg):
        i + 1
    restime = time.perf_counter() - start - intemptycycle(arg)
    opers = math.floor(arg / restime)
    return(opers)


def intminus(arg):
    start = time.perf_counter()
    for i in range(arg):
        i - 1
    restime = time.perf_counter() - start - intemptycycle(arg)
    opers = math.floor(arg / restime)
    return(opers)

def intmult(arg):
    start = time.perf_counter()
    for i in range(arg):
        i*9
    restime = time.perf_counter() - start - intemptycycle(arg)
    opers = math.floor(arg / restime)
    return(opers)

def intdiv(arg):
    start = time.perf_counter()
    for i in range(arg):
        i//9
    restime = time.perf_counter() - start - intemptycycle(arg)
    opers = math.floor(arg / restime)
    return(opers)

def floatplus(arg):
    start = time.perf_counter()
    for i in range(arg):
        float(i) + 1
    restime = time.perf_counter()- start - floatemptycycle(arg)
    opers = math.floor(arg / restime)
    return opers

def floatminus(arg):
    start = time.perf_counter()
    for i in range(arg):
        float(i) - 1
    restime = time.perf_counter() - start - floatemptycycle(arg)
    opers = math.floor(arg / restime)
    return opers

def floatmult(arg):
    start = time.perf_counter()
    for i in range(arg):
        float(i) * 10
    restime = time.perf_counter() - start - floatemptycycle(arg)
    opers = math.floor(arg / restime)
    return opers

def floatdiv(arg):
    start = time.perf_counter()
    for i in range(arg):
        float(i) /10
    restime = time.perf_counter() - start - floatemptycycle(arg)
    opers = math.floor(arg / restime)
    return opers

def intemptycycle(arg):
    start = time.perf_counter()
    for i in range(arg):
        i
    return(time.perf_counter()- start)

def floatemptycycle(arg):
    start = time.perf_counter()
    for i in range(arg):
        float(i)
    return(time.perf_counter()- start)

