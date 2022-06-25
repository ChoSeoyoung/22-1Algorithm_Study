# 3009, Bronze 3
# https://www.acmicpc.net/problem/3009

import sys

X=[]
Y=[]

for i in range(3):
    x,y=map(int, sys.stdin.readline().split())
    if x not in X:
        X.append(x)
    elif x in X:
        X.remove(x)
    if y not in Y:
        Y.append(y)
    elif y in Y:
        Y.remove(y)
    
print(X[0],Y[0])
    