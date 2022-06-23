# 1427, Silver 5
# https://www.acmicpc.net/problem/1427

import sys

S=sys.stdin.readline().rstrip()
llist=[]
for s in S:
    llist.append(int(s))
llist=list(map(str,sorted(llist,reverse=True)))
print((''.join(llist)))
