# 1620, Silver 4
# https://www.acmicpc.net/problem/1620

import sys

N,M=map(int,sys.stdin.readline().split())
D=dict()
for i in range(1,N+1):
    poketmon=sys.stdin.readline().rstrip()
    D[str(i)]=poketmon
    D[poketmon]=str(i)

llist=[sys.stdin.readline().rstrip() for _ in range(M)]
for i in llist:
    print(D[i])