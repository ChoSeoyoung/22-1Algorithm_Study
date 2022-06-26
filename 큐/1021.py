# 1021, Silver 4
# https://www.acmicpc.net/problem/1021

import sys
from collections import deque

N,M=map(int, sys.stdin.readline().split())
llist=deque([i for i in range(1,N+1)])
targets=deque(list(map(int, sys.stdin.readline().rstrip().split())))

cnt=0
while targets:
    target=targets.popleft()
    for i in range(len(llist)):
        if target==llist[i]:
            idx=i
    
    if(idx<len(llist)-idx):
        while True:
            n=llist.popleft()
            if(n==target):
                break
            else:
                cnt+=1
                llist.append(n)
    else:
        while True:
            n=llist.pop()
            if(n==target):
                cnt+=1
                break
            else:
                cnt+=1
                llist.appendleft(n)

print(cnt)