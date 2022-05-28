# 1931, 회의실 배정, Silver 1
# https://www.acmicpc.net/problem/1931

import sys
N = int(sys.stdin.readline())
S = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
S = sorted(S,key=lambda x:x[0])

def is_available(S1, S2):
    if(S1[1]<S[0]):
        return True

def greedy(S):
    sstack=[]
    
    for meeting in S:
        flag=1
        for i in range(len(sstack)):
            if(sstack[i][-1][1]<meeting[0]):
                sstack[i].append(meeting)
        
        if(flag==1):
            sstack.append([meeting])
    
    sorted_sstack=sorted(sstack, key=lambda x:len(x), reverse=True)
    return len(sorted_sstack[0])

print(greedy(S))