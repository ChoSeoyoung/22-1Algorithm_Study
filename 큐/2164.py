# 2164, Silver 4
# https://www.acmicpc.net/problem/2164

import sys
from collections import deque

N=int(sys.stdin.readline())
Q=deque([i for i in range(1, N+1)])

while len(Q)!=1:
    Q.popleft()
    Q.append(Q.popleft())

print(Q.popleft())