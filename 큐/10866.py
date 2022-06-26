# 10866, Silver 4
# https://www.acmicpc.net/problem/10866

import sys
from collections import deque

N=int(sys.stdin.readline())
Q=deque([])
result=[]
for i in range(N):
    command=sys.stdin.readline().rstrip().split()
    if command[0]=='push_back':
        Q.append(command[1])
    elif command[0]=='push_front':
        Q.appendleft(command[1])
    elif command[0]=='pop_back':
        if len(Q)==0:
            result.append(-1)
        else:
            result.append(Q.pop())
    elif command[0]=='pop_front':
        if len(Q)==0:
            result.append(-1)
        else:
            result.append(Q.popleft())
    elif command[0]=='back':
        if len(Q)==0:
            result.append(-1)
        else:
            result.append(Q[-1])
    elif command[0]=='front':
        if len(Q)==0:
            result.append(-1)
        else:
            result.append(Q[0])
    elif command[0]=='size':
        result.append(len(Q))
    elif command[0]=='empty':
        if len(Q)==0:
            result.append(1)
        else:
            result.append(0)
    
for i in result:
    print(i)
    