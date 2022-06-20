# 10809, Bronze 5
# https://www.acmicpc.net/problem/10809

import sys

S=sys.stdin.readline().rstrip()
D=dict()
for s in 'abcdefghijklmnopqrstuvwxyz':
    D[s]=-1

for i in range(len(S)-1,-1,-1):
    D[S[i]]=i

for s in 'abcdefghijklmnopqrstuvwxyz':
    print(D[s],end=' ')