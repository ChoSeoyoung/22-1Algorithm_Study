# 12865, 평범한 배낭
# https://www.acmicpc.net/problem/12865
# Branch-and-Bounds

import sys
from queue import Empty, PriorityQueue

n, W = map(int, sys.stdin.readline().split())
llist=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]
llist=sorted(llist, key=lambda x: round(x[1]/x[0],2), reverse=True)
w,v=[],[]

N=0
for i in range(n):
    if llist[i][0]<=W:
        w.append(llist[i][0])
        v.append(llist[i][1])
        N+=1
print(w,v)        

maxprofit=0

def value(weight, profit, idx):
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
    #print("value:", weight, profit, idx, bound)
    return bound

def knapsack(weight, profit, idx):
    global maxprofit
    #Initialize Priority Queue
    Q = PriorityQueue()
    #euqueue root
    Q.put((value(weight, profit, idx)*(-1),[weight, profit, idx]))
    while(Q.qsize()!=0):
        u=Q.get()
        best=u[0]
        ww,vv,i=u[1]
        print(ww,vv,i)
        if(maxprofit<vv):
            maxprofit=vv
        
        if(i==N):
            break
        elif(i<=N-1):
            if(ww+w[i]<=W):
                #print("append", value(ww+w[i],vv+v[i],i+1),ww+w[i],vv+v[i],i+1)
                Q.put((value(ww+w[i],vv+v[i],i+1)*(-1),[ww+w[i],vv+v[i],i+1]))
            #print("append", value(ww,vv,i+1),ww,vv,i+1)
            Q.put((value(ww,vv,i+1)*(-1),[ww, vv, i+1]))

    return maxprofit
        
print(knapsack(0, 0, 0))
