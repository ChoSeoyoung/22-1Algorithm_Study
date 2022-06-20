# 2675, Bronze 2
# https://www.acmicpc.net/problem/2675

import sys

N=int(sys.stdin.readline())
llist=[sys.stdin.readline().split() for _ in range(N)]

for tmp in llist:
    for s in tmp[1]:
        for i in range(int(tmp[0])):
            sys.stdout.write(s)
    sys.stdout.write('\n')