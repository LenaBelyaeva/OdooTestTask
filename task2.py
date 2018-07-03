import string
import random

def foo():
    toprint = ""
    seq = {}
    i = 0
    while (i < 1e6):
        c = random.choice(string.ascii_lowercase)
        conditions = {c : 4e4}
        if len(toprint) > 0:
            cc = toprint[-1] + c
            conditions[cc] = 2e3
        if len(toprint) > 1:
            ccc = toprint[-2] + cc
            conditions[ccc] = 100
        for x in conditions.keys():
             if (x in seq.keys() and seq[x] >= conditions[x]):
                continue        
        for x in conditions.keys():
            if (x in seq.keys()):
                seq[x] += 1
            else:
                seq[x] = 1
        toprint += c
        i += 1
        if len(toprint) > 1000:
            print (toprint[:-3], end = '')
            toprint = toprint[-3:]
    print (toprint, end = '', flush = True)


foo()
