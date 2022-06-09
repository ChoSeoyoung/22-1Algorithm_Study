# 12865, 평범한 배낭
# https://www.acmicpc.net/problem/12865
# Backtracking

import sys

N, W = map(int, sys.stdin.readline().split())
llist=[list(map(int, sys.stdin.readline().split())) for _ in range(N)]
llist=sorted(llist, key=lambda x: round(x[1]/x[0],2), reverse=True)
w,v=[0 for _ in range(N)],[0 for _ in range(N)]
for i in range(N):
    w[i],v[i]=llist[i][0],llist[i][1]

#BFS 방식의 탐색, 너비 우선 탐색
maxprofit=0

def promising(weight, profit, idx):
    global maxprofit
    #무게를 추가했더니 weight를 넘어설 때
    if(weight+w[idx]>W):
        return False
    else:
        j=idx
        totweight=weight
        bound=profit
        while(j<=N-1 and totweight+w[j]<=W):
            totweight+=w[j]
            bound+=v[j]
            j+=1
        k=j
        if(k<=N-1):
            bound+=(W-totweight)*(v[k]/w[k])
        return bound>maxprofit

def knapsack(weight, profit, idx):
    global maxprofit
    if(profit> maxprofit and weight<=W):
        maxprofit = profit
    
    if(idx<N):
        if(promising(weight, profit, idx)):
            knapsack(weight+w[idx], profit+v[idx], idx+1)
            knapsack(weight,profit, idx+1)

knapsack(0, 0, 0)
print(maxprofit)
