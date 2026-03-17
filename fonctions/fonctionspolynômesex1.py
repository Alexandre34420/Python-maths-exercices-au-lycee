def racines(a,b,c):
    L=[]
    for x in range(-4,5):
        if a*x**2+b*x+c==0:
            L.append(x)
    return L

