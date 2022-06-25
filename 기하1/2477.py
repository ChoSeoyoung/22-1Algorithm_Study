# 2477, Silver 3
# https://www.acmicpc.net/problem/2477

import sys

N=int(sys.stdin.readline())
arr=[[] for i in range(6)]

W_idx=0
W_max=0
H_idx=0
H_max=0
for i in range(6):
    a,b=map(int,sys.stdin.readline().split())
    if a==1 or a==2:
       if b>W_max:
            W_max=b
            W_idx=i
    elif a==3 or a==4:
        if b>H_max:
            H_max=b
            H_idx=i
    arr[i]=[a,b]

big_W=arr[W_idx][1]
big_H=arr[H_idx][1]
small_W=abs(arr[((H_idx-1)%6)][1]-arr[((H_idx+1)%6)][1])
small_H=abs(arr[((W_idx-1)%6)][1]-arr[((W_idx+1)%6)][1])
print((big_W*big_H-small_W*small_H)*N)
