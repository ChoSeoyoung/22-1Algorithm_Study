# Silver 5
import sys

N=int(sys.stdin.readline())

def zero_count(r):
    cnt = 0
    arr = list(range(r[0],r[1]+1))
    
    for _ in arr:
        for n in str(_):
            if int(n) == 0:
                cnt+=1
    
    return cnt

for i in range(N):
    r=list(map(int, sys.stdin.readline().split()))
    print(zero_count(r))

#print(zero_count([0,10]))
#print(zero_count([33,1005]))
#print(zero_count([1,4]))
