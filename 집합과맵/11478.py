# 11478, Silver 3
# https://www.acmicpc.net/problem/11478

import sys

S=sys.stdin.readline().rstrip()
sset=set()

for i in range(0, len(S)):
    for j in range(0,len(S)-i):
        sset.add(S[j:j+i+1:1])

print(len(sset))