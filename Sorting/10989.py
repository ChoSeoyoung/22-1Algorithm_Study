# 10989, Bronze1
# https://www.acmicpc.net/problem/10989

import sys

N=int(sys.stdin.readline())
D=dict()
for _ in range(N):
    n=int(sys.stdin.readline())
    if n not in D:
        D[n]=1
    else:
        D[n]+=1

for k,v in sorted(D.items(), key=lambda x:x[0]):
    for _ in range(v):
        print(k)