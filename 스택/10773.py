# 10773, Silver 4
# https://www.acmicpc.net/problem/10773

import sys

N=int(sys.stdin.readline())
S=[]
for i in range(N):
    n=int(sys.stdin.readline())
    if n==0:
        if len(S)!=0:
            S.pop()
    else:
        S.append(n)

print(sum(S))