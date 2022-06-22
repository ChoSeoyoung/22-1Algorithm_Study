# 1541, Silver 2
# https://www.acmicpc.net/problem/1541

import sys

llist=sys.stdin.readline().rstrip().split('-')
llist2=[i.split('+') for i in llist]
llist3=[]
for i in llist2:
    sum=0
    for ii in i:
        sum+=int(ii)
    llist3.append(sum)

result=llist3[0]
for i in llist3[1:]:
    result=result-int(i)

print(result)