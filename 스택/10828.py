# 10828, Silver 4
# https://www.acmicpc.net/problem/10828

import sys

N=int(sys.stdin.readline())

S=[]
result=[]
for i in range(N):
    cmd=sys.stdin.readline().split()
    if cmd[0]=='push':
        S.append(cmd[1])
    elif cmd[0]=='top':
        if len(S)==0:
            result.append(-1)
        else:
            result.append(S[-1])
    elif cmd[0]=='size':
        result.append(len(S))
    elif cmd[0]=='empty':
        if len(S)==0:
            result.append(1)
        else:
            result.append(0)
    elif cmd[0]=='pop':
        if len(S)==0:
            result.append(-1)
        else:
            result.append(S.pop())

for i in result:
    print(i)