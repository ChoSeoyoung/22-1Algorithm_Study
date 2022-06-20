# 11720
# https://www.acmicpc.net/problem/11720

import sys

N=int(sys.stdin.readline())
S=sys.stdin.readline().rstrip()

sum=0
for n in S:
    sum+=int(n)

print(sum)
