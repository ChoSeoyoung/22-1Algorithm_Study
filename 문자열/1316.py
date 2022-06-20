# 1316, Silver 5
# https://www.acmicpc.net/problem/1316

import sys

N=int(sys.stdin.readline())

cnt=0
for n in range(N):
    for S in sys.stdin.readline().split():
        flag=1
        D=dict()
        D[S[0]]=1
        for i in range(1, len(S)):
            if S[i] not in D:
                D[S[i]]=1
            elif S[i] in D:
                if S[i-1]!=S[i]:
                    flag=0
    if flag:
        cnt+=1

print(cnt)