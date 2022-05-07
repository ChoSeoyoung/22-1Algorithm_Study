# 1966, 1966, Silver 3
# https://www.acmicpc.net/problem/1966

import sys

N=int(sys.stdin.readline())
#N=0

def print_seq(total_num, doc_idx, arr):
    cnt=1

    idx=0
    while(idx<=len(arr)):        
        flag=1
        for i in range(idx+1, len(arr)):
            if(arr[idx]<arr[i]):
                flag=0
                break
        if(flag==1): #우선순위가 가장 높으면 인쇄
            if(idx==doc_idx):
                return cnt
            idx+=1
            cnt+=1
        else: #뒤에 우선순위가 더 높은 문서가 있으면
            if(idx==doc_idx):
                doc_idx=len(arr)
            arr.append(arr[idx])
            idx+=1
        

for i in range(N):
    total_num, doc_idx=map(int,sys.stdin.readline().split())
    arr=list(map(int,sys.stdin.readline().split()))
    print(print_seq(total_num, doc_idx, arr))

#print(print_seq(1,0,[5]))
#print(print_seq(4,2,[1,2,3,4]))
#print(print_seq(6,0,[1,1,9,1,1,1]))