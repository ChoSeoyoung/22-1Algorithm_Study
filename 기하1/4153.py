# 4153, Bronze 3
# https://www.acmicpc.net/problem/4153

import sys

llist=[]
while True:
    a,b,c=map(int, sys.stdin.readline().split())
    if a==0 and b==0 and c==0:
        break
    llist.append((a,b,c))
    
for a,b,c in llist:
    tmp=sorted([a,b,c])
    A,B,C=tmp[0],tmp[1],tmp[2]
    if C*C==A*A+B*B:
        print("right")
    else:
        print("wrong")