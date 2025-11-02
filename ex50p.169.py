from random import *
def robot():
    x=0
    y=0
    for i in range(2):
        a=random() # un nombre aléatoire entre 0 et 1.
        if a<=0.5:
         x=x+1
        if 0.5<a<=0.6:
         x=x-1
        if 0.6<a<=0.85:
         y=y+1
        if a>0.85:
         y=y-1
    return(x,y)


