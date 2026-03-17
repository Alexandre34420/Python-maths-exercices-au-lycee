u=500
L=[500]
for i in range(100):
    u=0.998*u+1.2
    L.append(u)
print(L)
