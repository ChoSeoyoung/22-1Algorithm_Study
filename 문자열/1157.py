# 1157, Bronze1
# https://www.acmicpc.net/problem/1157

import sys

S=sys.stdin.readline().rstrip().lower()

D={}

for s in S:
    if s in D:
        D[s]+=1
    else:
        D[s]=1

max_key=''
max_cnt=-1
for k,v in reversed(sorted(D.items(),key=lambda x:x[1])):
    if v>max_cnt:
        max_cnt=v
        max_key=k
    elif v==max_cnt:
        max_key='?'
        break
    else:
        break

print(max_key.upper())