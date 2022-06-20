# 2908, Bronze 2
# https://www.acmicpc.net/problem/2908

import sys

llist=[]
for ss in sys.stdin.readline().split():
    num=''
    for s in reversed(ss):
        num+=s
    llist.append(int(num))

print(max(llist))