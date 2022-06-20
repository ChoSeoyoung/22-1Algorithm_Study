# 1655, Gold 2
# https://www.acmicpc.net/problem/1655
# -1 (0 1)/ 2 -1 1 2
import sys
from queue import PriorityQueue

N=int(sys.stdin.readline())
llist=[int(sys.stdin.readline()) for _ in range(N)]
max_Q=PriorityQueue() #small Q
min_Q=PriorityQueue() #big Q


for num in llist:
    if min_Q.qsize()==0 and max_Q.qsize()==0:
        mid_num=num
        max_Q.put(num*(-1))
        sys.stdout.write(str(mid_num))
        sys.stdout.write('\n')
    else:
        if max_Q.qsize()!=0 and min_Q.qsize()==0:
            max_num=(max_Q.get()*-1)
            if num<=max_num:
                mid_num=num
                sys.stdout.write(str(mid_num))
                sys.stdout.write('\n')
                max_Q.put(mid_num*-1)
                min_Q.put(max_num)
            elif num>max_num:
                mid_num=max_num
                sys.stdout.write(str(mid_num))
                sys.stdout.write('\n')
                max_Q.put(max_num*-1)
                min_Q.put(num)
        elif max_Q.qsize()==0 and min_Q.qsize()!=0:
            min_num=min_Q.get()
            if num>=min_num:
                mid_num=min_num
                sys.stdout.write(str(mid_num))
                sys.stdout.write('\n')
                max_Q.put(min_num*-1)
                min_Q.put(mid_num)
            elif num<min_num:
                mid_num=num
                sys.stdout.write(str(mid_num))
                sys.stdout.write('\n')
                max_Q.put(mid_num*-1)
                min_Q.put(max_num)
        elif max_Q.qsize()==min_Q.qsize() and max_Q.qsize()!=0 and min_Q.qsize()!=0:
            max_num=max_Q.get()*-1
            min_num=min_Q.get()
            if num<=max_num:
                max_Q.put(num*-1)
                max_Q.put(max_num*-1)
                min_Q.put(min_num)
            elif max_num<num and num<min_num:
                max_Q.put(max_num*-1)
                max_Q.put(num*-1)
                min_Q.put(min_num)
            else:
                max_Q.put(max_num*-1)
                max_Q.put(min_num*-1)
                min_Q.put(num)
            mid_num=max_Q.get()*-1
            sys.stdout.write(str(mid_num))
            sys.stdout.write('\n')
            max_Q.put(mid_num*-1)
        elif max_Q.qsize()>min_Q.qsize() and max_Q.qsize()!=0 and min_Q.qsize()!=0:
            # 1 2/ 5   10, 2 5 10
            max_num=max_Q.get()*-1
            min_num=min_Q.get()
            if num<=max_num:
                max_Q.put(num*-1)
                min_Q.put(max_num)
                min_Q.put(min_num)
            elif max_num<num and num<min_num:
                # max num min num num
                max_Q.put(max_num*-1)
                min_Q.put(num)
                min_Q.put(min_num)
            else: # max num min num num
                max_Q.put(max_num*-1)
                min_Q.put(min_num)
                min_Q.put(num)
            mid_num=max_Q.get()*-1
            sys.stdout.write(str(mid_num))
            sys.stdout.write('\n')
            max_Q.put(mid_num*-1)