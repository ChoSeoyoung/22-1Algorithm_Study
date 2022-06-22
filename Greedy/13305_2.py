# 13305, Silver 4
# https://www.acmicpc.net/problem/13305

import sys

N=int(sys.stdin.readline())
dist_list=list(map(int,sys.stdin.readline().rstrip().split()))+[0]
city_list=list(map(int,sys.stdin.readline().rstrip().split()))

min_cost=city_list[0]
for i in range(1,len(city_list)):
    if (min_cost>=city_list[i]):
        min_cost=city_list[i]
    else:
        city_list[i]=min_cost

total_cost=0
for i in range(len(dist_list)):
    total_cost+=dist_list[i]*city_list[i]

print(total_cost)