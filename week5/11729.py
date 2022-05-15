# 11729, 하노이 탑 이동 순서, Silver 1
# https://www.acmicpc.net/problem/11729

cnt=0
result=[]

# 123 0 0
# 3   0  12
# 12  0  0
# 2   0   1
# 0   12 # 
def hanoi(n, src, tmp, des):
    global cnt
    cnt=cnt+1
    if(n>1):
        hanoi(n-1, src, des, tmp)
        result.append((src, des))
        hanoi(n-1, tmp, src, des)
    else:#n==1
        result.append((src, des))

    
hanoi(3, 1,2,3)
print(cnt)
for item in result:
    print(item[0], item[1])