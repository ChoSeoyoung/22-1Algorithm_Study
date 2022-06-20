# 1655, Gold 2
# https://www.acmicpc.net/problem/1655
# -1 (0 1)/ 2 -1 1 2
import sys
from queue import PriorityQueue
import heapq

N=int(sys.stdin.readline())
llist=[int(sys.stdin.readline()) for _ in range(N)]
max_Q=[] #small Q
min_Q=[] #big Q

for num in llist:
    if len(min_Q)==0 and len(max_Q)==0:
        mid_num=num
        heapq.heappush(max_Q,num*(-1))
        sys.stdout.write(str(mid_num))
        sys.stdout.write('\n')
    else:
        if len(max_Q)!=0 and len(min_Q)==0:
            max_num=(heapq.heappop(max_Q)*-1)
            if num<=max_num:
                mid_num=num
                sys.stdout.write(str(mid_num))
                sys.stdout.write('\n')
                heapq.heappush(max_Q,mid_num*-1)
                heapq.heappush(min_Q, max_num)
            elif num>max_num:
                mid_num=max_num
                sys.stdout.write(str(mid_num))
                sys.stdout.write('\n')
                heapq.heappush(max_Q, max_num*-1)
                heapq.heappush(min_Q, num)
        elif len(max_Q)==0 and len(min_Q)!=0:
            #min_num=min_Q[0]
            min_num=heapq.heappop(min_Q)
            if num>=min_num:
                mid_num=min_num
                sys.stdout.write(str(mid_num))
                sys.stdout.write('\n')
                heapq.heappush(max_Q, min_num*-1)
                heapq.heappush(min_Q, mid_num)
            elif num<min_num:
                mid_num=num
                sys.stdout.write(str(mid_num))
                sys.stdout.write('\n')
                heapq.heappush(max_Q, mid_num*-1)
                heapq.heappush(min_Q, max_num)
        elif len(max_Q)==len(min_Q) and len(max_Q)!=0 and len(min_Q)!=0:
            max_num=max_Q[0]*-1
            min_num=min_Q[0]
            #max_num=heapq.heappop(max_Q)*-1
            #min_num=heapq.heappop(min_Q)
            if num<=max_num:
                heapq.heappush(max_Q, num*-1)
                #heapq.heappush(max_Q, max_num*-1)
                #heapq.heappush(min_Q, min_num)
            elif max_num<num and num<min_num:
                #heapq.heappush(max_Q, max_num*-1)
                heapq.heappush(max_Q, num*-1)
                #heapq.heappush(min_Q,min_num)
            else:
                #heapq.heappush(max_Q, max_num*-1)
                min_num=heapq.heappop(min_Q)
                heapq.heappush(max_Q, min_num*-1)
                heapq.heappush(min_Q, num)
            sys.stdout.write(str(max_Q[0]*-1))
            sys.stdout.write('\n')
        elif len(max_Q)>len(min_Q)and len(max_Q)!=0 and len(min_Q)!=0:
            # 1 2/ 5   10, 2 5 10
            max_num=max_Q[0]*-1
            min_num=min_Q[0]
            #max_num=heapq.heappop(max_Q)*-1
            #min_num=heapq.heappop(min_Q)
            if num<=max_num:
                max_num=heapq.heappop(max_Q)*-1
                min_num=heapq.heappop(min_Q)
                heapq.heappush(max_Q, num*-1)
                heapq.heappush(min_Q, max_num)
                heapq.heappush(min_Q, min_num)
            elif max_num<num and num<min_num:
                # max num min num num
                #heapq.heappush(max_Q, max_num*-1)
                heapq.heappush(min_Q, num)
                #heapq.heappush(min_Q, min_num)
            else: # max num min num num
                #heapq.heappush(max_Q, max_num*-1)
                #heapq.heappush(min_Q, min_num)
                heapq.heappush(min_Q, num)
            sys.stdout.write(str(max_Q[0]*-1))
            sys.stdout.write('\n')