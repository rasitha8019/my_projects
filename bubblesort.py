def bubble(list):
    for i in range(len(list)-1):#O(n)
        for j in range(len(list)-i-1):#O(n )
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
    return list
print(bubble([5,9,3,1,2,8,4,7,6]))