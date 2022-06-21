# 7568, Silver 5
# https://www.acmicpc.net/problem/7568

import sys

N=int(sys.stdin.readline())
llist=[list(map(int, sys.stdin.readline().split())) for i in range(N)]

result=[0 for i in range(N)]
for i in range(len(llist)):
    sum=1
    for j in range(len(llist)):
        if i!=j:
            if llist[i][0]<llist[j][0] and llist[i][1]<llist[j][1]:
                sum+=1
    result[i]=str(sum)

s=' '.join(result)
print(s)
    