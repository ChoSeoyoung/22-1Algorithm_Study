# 13305, Silver 4
# https://www.acmicpc.net/problem/13305

import sys

N=int(sys.stdin.readline())
dis_list=list(map(int,sys.stdin.readline().rstrip().split()))+[0]
city_list=list(map(int,sys.stdin.readline().rstrip().split()))
city_D=dict()
for i in range(N):
    city_D[i]=city_list[i]
city=sorted(city_D.items(), key=lambda x:x[1])
#city=city_D.items()

s_city=N #shortest city
total_value=0
for c in city:
    if c[0]<s_city:
        for i in range(c[0], s_city):
            total_value+=c[1]*dis_list[i]
            dis_list[i]=0
        s_city=c[0]+1
    
    if sum(dis_list[1:])==0:
        break

for i in range(0, s_city):
    total_value+=city_D[0]*dis_list[i]
    dis_list[i]=0

print(total_value)