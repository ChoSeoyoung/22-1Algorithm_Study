# 11399, Silver 4
# https://www.acmicpc.net/problem/11399

import sys

N=int(sys.stdin.readline())
time_to_wait=list(map(int,sys.stdin.readline().rstrip().split()))
time_to_wait=sorted(time_to_wait)

total=0
for i in range(len(time_to_wait)):
    sum=0
    for j in range(0, i+1):
        sum+=time_to_wait[j]
    total+=sum
    
print(total)