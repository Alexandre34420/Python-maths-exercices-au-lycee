from random import *
def gain():
    x=0
    for i in range(4):
        x=x+randint(0,1)
        if x==0 or x==3:
            gain=2
        if x==1:
            gain=3
        if x==2:
            gain=1
        if x==4:
            gain=10
        return gain
