# 11650, Silver 5
# https://www.acmicpc.net/problem/11650

import sys

N=int(sys.stdin.readline())
llist=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
llist=sorted(llist, key=lambda x:x[1])
llist=sorted(llist, key=lambda x:x[0])

for i in llist:
    for j in i:
        print(j, end=' ')
    print()