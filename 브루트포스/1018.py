# 1018, Silver 4
# acmicpc.net/problem/1018

import sys
from copy import deepcopy

H, W = map(int, sys.stdin.readline().split())

B=[]
for i in range(0,H):
    B.append([])
    S=sys.stdin.readline().rstrip()
    for s in S:
        B[i].append(s)


min_cnt=99999
#시작이 B가 되도록 조정
for i in range(0, W-8+1):
    for j in range(0, H-8+1):
        #print(i,j)#,시작지점
        cnt=0
        board=deepcopy(B)
        for h in range(j, j+7,2):
            for w in range(i, i+7, 2):
                if board[h][w]!='B':
                    board[h][w]='B'
                    cnt+=1
                if board[h][w+1]!='W':
                    board[h][w+1]='W'
                    cnt+=1
                if board[h+1][w]!='W':
                    board[h+1][w]='W'
                    cnt+=1
                if board[h+1][w+1]!='B':
                    board[h+1][w+1]='B'
                    cnt+=1
        if min_cnt>cnt:
            min_cnt=cnt

#시작이 W가 되도록 조정
for i in range(0, W-8+1):
    for j in range(0, H-8+1):
        #print(i,j)#,시작지점
        cnt=0
        board=deepcopy(B)
        for h in range(j, j+7,2):
            for w in range(i, i+7, 2):
                if board[h][w]!='W':
                    board[h][w]='W'
                    cnt+=1
                if board[h][w+1]!='B':
                    board[h][w+1]='B'
                    cnt+=1
                if board[h+1][w]!='B':
                    board[h+1][w]='B'
                    cnt+=1
                if board[h+1][w+1]!='W':
                    board[h+1][w+1]='W'
                    cnt+=1
        if min_cnt>cnt:
            min_cnt=cnt

print(min_cnt)
