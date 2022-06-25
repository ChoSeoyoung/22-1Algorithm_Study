# 1085, Bronze 3
# https://www.acmicpc.net/problem/1085

import sys

x,y,w,h=map(int,sys.stdin.readline().split())
print(min(x,y,w-x,h-y))