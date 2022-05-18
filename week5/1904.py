# 1904, 01타일, Silver3
# https://www.acmicpc.net/problem/1904
# 피보나치

#2, 00, 11
#3, 001, 100, 111 1+2=3
#4, 0000, 0011, 1001, 1100, 1111 1+3+1, B[4][0]+B[3][1]+B[2][2] 5
#5, 00001, 00100, 10000, 00111, 10011, 11001, 11100, 11111 1+4+3 8
#6, 000000, 110000, 100001, 000011, B[6][0]+B[5][1]+B[4][2]+B[3][3]=1+5+6+1=13
#B[i][j]=B[i-1][j-1]+B[i-1][j]

import sys

N=int(sys.stdin.readline())

B=[0 for i in range(1000001)]
B[0]=0
B[1]=1
B[2]=2
for i in range(3,N+1):
    B[i]=(B[i-1]+B[i-2])%15746

print(B[N])

