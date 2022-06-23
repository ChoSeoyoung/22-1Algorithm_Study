# 1269, Silver 3
# https://www.acmicpc.net/problem/1269

import sys

N,M=map(int, sys.stdin.readline().split())
A=set(list(map(int, sys.stdin.readline().split())))
B=set(list(map(int, sys.stdin.readline().split())))
A_B=A.intersection(B)

print(len(A)+len(B)-2*len(A_B))
