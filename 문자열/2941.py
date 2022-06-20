# 2941, Silver 5
# https://www.acmicpc.net/problem/2941

import sys

S=sys.stdin.readline().rstrip()
croatia=["c=","c-","dz=","d-","lj","nj","s=","z="]

for i in croatia:
    S=S.replace(i,"*")

print(len(S))