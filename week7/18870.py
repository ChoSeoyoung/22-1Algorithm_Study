# 18870, 좌표 압축, Silver 2
# https://www.acmicpc.net/problem/18870

import sys

N=int(sys.stdin.readline())
S=list(map(int, sys.stdin.readline().split()))
sorted_S=sorted(set(S))
dd=dict()
for i in range(len(sorted_S)):
    if sorted_S[i] not in dd:
        dd[sorted_S[i]]=i
for i in S:
    print(dd[i], end=' ')