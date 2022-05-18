# 1197, 최소 스패닝 트리, Gold 4
# https://www.acmicpc.net/problem/1197

import sys

INF = 2147483648
N1, N2 = map(int, sys.stdin.readline().split())
graph = [[INF for _ in range(N1)] for _ in range(N1)]
for _ in range(N1):
    v1, v2, val = map(int, sys.stdin.readline().split())
    graph[v1-1][v2-1] = val
    graph[v2-1][v1-1] = val

#Prim's Algorithm
def prim(N, W):
    F=[]
    #다음에 갈 vertex
    vnear=0
    #현재 vertex에서 다른 vertex까지의 거리
    #INF이면 연결되지 않은 노드
    distance=[INF for i in range(N)]
    #각 vertex에서 가장 가까운 노드
    #-1이면 이미 방문한 노드
    nearest = [0 for i in range(N)]

    #시작정점 vertex 0에서 시작
    for i in range(1, N1, 1):
        distance[i] = graph[0][i]
        nearest[i]=0

    #N-1개의 간선을 찾을 때까지 반복
    while(len(F)!=N-1):
        min=INF
        tmp=vnear
        for i in range(1, N, 1):
            if(distance[i]<min and nearest[i]!=-1):
                min=distance[i]
                vnear=i
        F.append({(tmp,vnear):distance[vnear]})
        distance[vnear]=INF
        
        #다음 vertex를 기준으로 초기화
        for i in range(1, N, 1):
            if(W[i][vnear]<distance[i]):
                distance[i]=W[i][vnear]
                nearest[i]=vnear
    
    return F

#Kruskal's Algorithm
disjoint_set = []
distance = dict()

def initial(N):
    for i in range(0,N):
        disjoint_set.append({i})

def find(idx):
    for sset in disjoint_set:
        if idx in sset:
            return sset

def merge(set_a, set_b):
    disjoint_set.remove(set_a)
    disjoint_set.remove(set_b)
    disjoint_set.append(set_a.union(set_b))

def kruskal(N, W):
    F=[]

    initial(N)
    #이음선을 가중치가 작은 것부터 차례로 정렬
    for i in range(len(W)):
        for j in range(i+1,len(W[i])):
            if(W[i][j]!=0):
                if W[i][j] not in distance:
                    distance[W[i][j]]=[]
                    distance[W[i][j]].append((i,j))
                else:
                    distance[W[i][j]].append((i,j))

    no_edge=0
    while(no_edge < N-1):
        tmp_key=sorted(distance)[0]
        tmp=distance.pop(tmp_key)
        a,b=tmp.pop()
        p = find(a)
        q = find(b)
        if(p!=q):
            merge(p, q)
            F.append({(a,b):tmp_key})
            no_edge+=1
        if tmp!=[]:
            distance[tmp_key]=tmp
    
    return F

#print(prim(N1, graph))
#print(kruskal(N1,graph))
result=prim(N1, graph)
min_total=0
for dd in result:
    for val in dd.values():
        min_total+=val

print(min_total)