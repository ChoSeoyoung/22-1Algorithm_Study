# 14425, Silver 3
# https://www.acmicpc.net/problem/14425

import sys

N,M = map(int, sys.stdin.readline().split())
S=set()
for _ in range(N):
    S.add(sys.stdin.readline().rstrip())
llist=[sys.stdin.readline().rstrip() for _ in range(M)]

cnt=0
for s in llist:
    if s in S:
        cnt+=1

print(cnt)