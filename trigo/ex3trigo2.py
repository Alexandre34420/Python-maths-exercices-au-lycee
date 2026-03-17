from math import*
def nb_tours(x):
    k=0
    while x>pi:
        x=x-2*pi
        k=k-1
    while x<=-pi:
        x=x+2*pi
        k=k+1
    return k


