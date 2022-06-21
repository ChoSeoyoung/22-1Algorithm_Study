# 22, Bronze 2
# https://www.acmicpc.net/problem/2798

import sys
import itertools

N,lim=map(int, sys.stdin.readline().split())
llist=map(int, sys.stdin.readline().split())

D=set()
for i in itertools.combinations(llist,3):
    n=sum(i)-lim
    if n<=0:
        D.add(n)

print(max(D)+lim)