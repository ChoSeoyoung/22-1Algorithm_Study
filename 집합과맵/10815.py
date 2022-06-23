# 10815, Silver 5
# https://www.acmicpc.net/problem/10815

import sys

N=int(sys.stdin.readline())
S=set(list(map(int, sys.stdin.readline().rstrip().split(' '))))

M=int(sys.stdin.readline())
llist=list(map(int, sys.stdin.readline().rstrip().split(' ')))
for i in llist:
    if i in S:
        print(1, end=' ')
    else:
        print(0, end=' ')