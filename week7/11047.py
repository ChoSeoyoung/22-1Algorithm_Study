# 11047, 동전 0, Silver 3
# https://www.acmicpc.net/problem/11047

import sys

N, amount = map(int, sys.stdin.readline().split())
S = sorted([int(sys.stdin.readline()) for _ in range(N)])

def greedy(S, amount):
    total_cnt=0
    cur_amt=0

    while True:
        #선택 과정
        tmp=S.pop()
        
        #적절성 확인
        while(tmp+cur_amt<=amount):
            total_cnt+=1 
            cur_amt+=tmp

        #해답 검사
        if(cur_amt==amount):
            break


    return total_cnt

print(greedy(S, amount))
