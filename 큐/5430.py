# 5430, Gold 5
# https://www.acmicpc.net/problem/5430

import sys
from collections import deque

N=int(sys.stdin.readline())
results=[]

for _ in range(N):
    ##command 배열 입력
    command=[]
    flag=1
    for c in sys.stdin.readline().rstrip():
        command.append(c)

    ##숫자 배열 입력
    M=int(sys.stdin.readline())
    llist=deque([])
    S=sys.stdin.readline().rstrip()
    if M!=0:
        for i in (S[1:-1]).split(','):
            llist.append(i)

    ##command 명령 수행
    for c in command:
        if c=='R':
            if flag==1:
                flag=0
            else:
                flag=1
        elif c=='D':
            if flag==1:
                if len(llist)==0:
                    llist='error'
                    break
                else:
                    llist.popleft()
            elif flag==0:
                if len(llist)==0:
                    llist='error'
                    break
                else:
                    llist.pop()
    if llist=='error':
            results.append(llist)
    else:
        if flag==1:
                results.append(llist)
        else:
            results.append(list(reversed(llist)))

for result in results:
    if result=='error':
        print(result)
    else:
        print(f"[{','.join(result)}]")