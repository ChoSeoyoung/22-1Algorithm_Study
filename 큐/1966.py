# 1966, Silver 3
# https://www.acmicpc.net/problem/1966

import sys
from collections import deque

testcase_cnt=int(sys.stdin.readline())
result=[]

for _ in range(testcase_cnt):
    N,M=map(int,sys.stdin.readline().split())
    cnt=0
    printer=deque(list(map(int, sys.stdin.readline().rstrip().split())))
    while M!=-1:
        # 2 1 3 2 <1>, 4, cnt=0
        # 2 3 3 <1> 2, 3, cnt=0
        # (3) 2 <1> 2 2, 2, cnt=1
        # (2) <1> 2, 1, cnt=2
        # 2 2 <1>, 0->2
        # (2) 2 <1>, 1, cnt=3
        # (2) <1>, 0, cnt=4
        now=printer.popleft()

        flag=0
        for i in printer:
            if i>now:
                flag=1
                break
        if flag==1:
            printer.append(now)
            if M==0:
                M=len(printer)-1
                continue
        else:
            cnt+=1

        M-=1

    result.append(cnt)

for i in result:
    print(i)

