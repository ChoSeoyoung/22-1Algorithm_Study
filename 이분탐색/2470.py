# 2470, Gold 5
# https://www.acmicpc.net/problem/2470

import sys

N=int(sys.stdin.readline())
llist=sorted(list(map(int,sys.stdin.readline().rstrip().split())))

high=len(llist)-1
low=0
minimum_diff=2000000001
a,b=(0,0)
while low<high:
    high_num=llist[high]
    low_num=llist[low]

    diff=high_num+low_num
    if abs(diff)<minimum_diff:
        minimum_diff=abs(diff)
        a,b=(low_num,high_num)


    if diff==0:
        a,b=(low_num,high_num)
        break
    elif diff>0:
        high-=1
    elif diff<0:
        low+=1
    

print(a,b)