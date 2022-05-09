# Silver 2

exp=input().split('-')

tmp=[]
for _ in exp:
    tmp.append(eval(_))
result=tmp[0]
for num in tmp[1:]:
    result=result-num

print(result)
