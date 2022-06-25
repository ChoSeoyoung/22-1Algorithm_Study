# 1002, Silver 3
# https://www.acmicpc.net/problem/1002
# https://www.acmicpc.net/board/view/89819

import sys
import math

N=int(sys.stdin.readline())
result=[]

for i in range(N):
    x1,y1,r1,x2,y2,r2=map(int, sys.stdin.readline().split())
    dist=math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
    if abs(r1-r2)<dist and dist<r1+r2:
        result.append(2)
    elif dist==r1+r2 or (dist==abs(r1-r2)!=0):
        result.append(1)
    elif dist<abs(r1-r2) or r1+r2<dist:
        result.append(0)
    elif x1==x2 and y1==y2 and r1==r2:
        result.append(-1)

for i in result:
    print(i)