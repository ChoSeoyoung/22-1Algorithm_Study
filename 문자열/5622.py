# 5622, Bronze 2
# https://www.acmicpc.net/problem/5622

import sys

S=sys.stdin.readline().rstrip()
alphabet={'':0, 'ABC':3, 'DEF':4, 'GHI':5, 'JKL':6, 'MNO':7, 'PQRS':8, 'TUV':9, 'WXYZ':10}
phone=dict()
for k,v in alphabet.items():
    for s in k:
        phone[s]=v

cnt=0
for s in S:
    cnt+=phone[s]

print(cnt)