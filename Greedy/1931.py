# 1931, 회의실 배정, Silver 1
# https://www.acmicpc.net/problem/1931

import sys

N = int(sys.stdin.readline())
S = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
S = sorted(S, key=lambda x:x[1]-x[0])
S = sorted(S,key=lambda x:x[0])
#print(S)

sstack=[]
for i in S:
    if len(sstack)==0:
        sstack.append(i)
    else:
        if sstack[-1][0]<=i[0] and sstack[-1][1]>i[1]:
            sstack.pop()
            sstack.append(i)
        elif sstack[-1][1]<=i[0]:
            sstack.append(i)

#print(sstack)
print(len(sstack))