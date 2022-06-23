# 10816, Silver 4
# https://www.acmicpc.net/problem/10816

import sys

N=int(sys.stdin.readline())
D=dict()
for i in list(map(int, sys.stdin.readline().split())):
    if i not in D:
        D[i]=1
    else:
        D[i]+=1

M=int(sys.stdin.readline())
llist=list(map(int, sys.stdin.readline().split()))
for i in llist:
    if i in D:
        print(D[i], end=' ')
    else:
        print(0, end=' ')
