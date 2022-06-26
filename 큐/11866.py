# 11866, Silver 5
# https://www.acmicpc.net/problem/11866

import sys
from collections import deque

N,K=map(int, sys.stdin.readline().split())
Q=deque([i for i in range(1, N+1)])

llist=[]
while len(Q)!=0:
    for i in range(K-1):
        Q.append(Q.popleft())
    llist.append(str(Q.popleft()))

print(f"<{', '.join(llist)}>")