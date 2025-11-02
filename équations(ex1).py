from math import* # importer la bibliothèque mathématique
def sol(c):
    if c<0:
        return "pas de solution"
    if c==0:
        return 0
    if c>0:
        return sqrt (c),-sqrt(c)
