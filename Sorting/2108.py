# 2108, Silver 3
# https://www.acmicpc.net/problem/2108

import sys
from collections import Counter

N=int(sys.stdin.readline())
llist=[int(sys.stdin.readline()) for _ in range(N)]
llist=sorted(llist)

print(round(sum(llist)/N))
print(llist[len(llist)//2])

if len(llist)==1:
    print(llist[0])
else:
    small, small2 = Counter(llist).most_common(2)
    if small[1]==small2[1]:
        print(small2[0])
    else:
        print(small[0])
print(llist[-1]-llist[0])

