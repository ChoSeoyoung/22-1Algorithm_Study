# 11725, Silver 2
# https://www.acmicpc.net/problem/11725

import sys

N=int(sys.stdin.readline())
parent=[-1 for i in range(N+1)]
G={}
##1. 그래프 초기화
for _ in range(N-1):
    a,b=map(int, sys.stdin.readline().split())
    if a not in G:
        G[a]=[]
    if b not in G[a]:
        G[a].append(b)
    
    if b not in G:
        G[b]=[]
    if b not in G[b]:
        G[b].append(a)

root=1
stack=[root]
visited=set([root])
while stack:
    node=stack.pop()
    for n in G[node]:
        if parent[n]==-1:
            parent[n]=node
        if n not in visited:
            stack.append(n)
            visited.add(n)


for i in parent[2:]:
    print(i)