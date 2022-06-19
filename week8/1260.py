# 1260
# https://www.acmicpc.net/problem/1260

from collections import deque
import sys

V, E, start= map(int, sys.stdin.readline().split())
G=dict({i:[] for i in range(1,V+1)})
for _ in range(E):
    a,b=map(int, sys.stdin.readline().split())
    G[a].append(b)
    G[b].append(a)
    
# 재귀함수 이용
discovered=[]
def DFS(graph, start):
    if start not in discovered:
        discovered.append(start)
        for i in sorted(G[start]):
            DFS(graph, i)

# 스택이용
discovered2=[]
def DFS2(graph, start):
    stack=[start]
    while stack:
        v=stack.pop()
        if v not in discovered2:
            discovered2.append(v)
            for i in sorted(G[v]):
                DFS2(graph, i)

# 큐 이용
discovered3=[]
def BFS(graph, start):
    Q=deque([start])
    while Q:
        v=Q.popleft()
        if v not in discovered3:
            discovered3.append(v)
            for i in sorted(G[v]):
                Q.append(i)

DFS(G, start)
#DFS2(G, start)
BFS(G, start)
for i in discovered:
    print(i, end=" ")
print()
for i in discovered3:
    print(i, end=" ")
#print(discovered2)
#print(discovered3)