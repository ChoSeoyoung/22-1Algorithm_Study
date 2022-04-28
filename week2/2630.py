#분할정복-미해결
arr=[[1, 1, 0, 0, 0, 0, 1, 1], [1, 1, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 0, 0, 0, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 1]]
arr2=[[[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 1, 1], [0, 0, 1, 1], [1, 1, 0, 0], [1, 1, 0, 0]], [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 1, 1], [0, 0, 1, 1], [1, 1, 0, 0], [1, 1, 0, 0]]]
#arr=[list(map(int,input().split())) for i in range(int(input()))]

result=[]
def divide_paper(arr):
    arr=list(map(lambda x:[sum(x)] if sum(x)==0 or sum(x)==len(x) else x, arr))
    if(len(list(filter((lambda x:len(x)==1),arr)))==len(arr)):
        return arr
    arr1,arr2,arr3,arr4=arr[:len(arr)//2],arr[len(arr)//2:],arr[:len(arr)//2],arr[len(arr)//2:]
    arr1=[arr[i][:len(arr1)] for i in range(len(arr1))]
    arr2=[arr[i][len(arr2):] for i in range(len(arr2))]
    arr3=[arr[i][:len(arr3)] for i in range(len(arr3))]
    arr4=[arr[i][len(arr4):] for i in range(len(arr4))]
    arr=[arr1]+[arr2]+[arr3]+[arr4]
    return arr

divide_paper(arr)
result=[sum(i) for i in arr]
print(result.count(0))
print(len(result)-result.count(0))

