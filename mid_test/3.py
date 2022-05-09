# Silver 3
import sys

#N=int(sys.stdin.readline())
N=10

dd={1:0,2:1,3:1,4:2,5:3}

for i in range(N+1):
    if(i>=6):
        tmp=dd[i-1]+1
        if((i%3)==0):
            tmp=min(tmp,dd[i//3]+1)
        elif((i%2)==0):
            tmp=min(tmp,dd[i//2]+1)
        dd[i]=tmp

print(dd[N])
