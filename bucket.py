import math
def bubble(list):
    for i in range(len(list)-1):#O(n)
        for j in range(len(list)-i-1):#O(n )
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
    return list
def bucket(list):
    noOfBuckets=round(math.sqrt(len(list)))
    maxValue=max(list)
    arr=[]
    for i in range(noOfBuckets):
        arr.append([])
    for j in list:
        index_b=math.ceil(j*noOfBuckets/maxValue)
        arr[index_b-1].append(j)
    for i in range(noOfBuckets):
        arr[i]=bubble(arr[i])
    k=0
    for i in range(noOfBuckets):
        for j in range(len(arr[i])):
            list[k]=arr[i][j]
            k+=1
    return list
print(bucket([5,3,4,7,2,8,6,9 ]))
