import sys

N, W = map(int, sys.stdin.readline().split())
llist=[list(map(int, sys.stdin.readline().split())) for _ in range(N)]
#llist=sorted(llist, key=lambda x: x[0],reverse=True)
D=dict()
for i in range(-1,N):
    D[i]={}

def knapsack(idx, weight):
    if weight in D[idx]:
        return D[idx][weight]
        
    if (idx==-1 and weight>0) or (idx>-1 and weight==0):
        D[idx][weight]=0
        return D[idx][weight]
    else:
        if idx-1>=-1:
            if weight-llist[idx][0]>=0:
                D[idx][weight]=max(knapsack(idx-1, weight),knapsack(idx-1,weight-llist[idx][0])+llist[idx][1])
                return D[idx][weight]
            else:
                D[idx][weight]=knapsack(idx-1,weight)
                return D[idx][weight]
        else:
            return 0

print(knapsack(N-1,W))