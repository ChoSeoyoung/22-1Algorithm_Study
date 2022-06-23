# 1764, Silver 4
# https://www.acmicpc.net/problem/1764

import sys

N,M=map(int, sys.stdin.readline().split())
A=set([sys.stdin.readline().rstrip() for _ in range(N)])
B=set([sys.stdin.readline().rstrip() for _ in range(M)])
A_B=A.intersection(B)
result=sorted(list(A_B))

print(len(result))
for name in result:
    print(name)