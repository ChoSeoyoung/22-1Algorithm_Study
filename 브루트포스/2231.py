# 2231, Bronze 2
# https://www.acmicpc.net/problem/2231

import sys
import itertools

N=int(sys.stdin.readline())

def constructor(N):
    sum=N
    length=len(str(N))
    llist=list(str(N))
    tmp=list(itertools.combinations(llist,1))
    for j in tmp:
        sum+=int(''.join(j))
    return sum

result=0
for i in range(1, N):
    if constructor(i)==N:
        result=i
        break
print(result)