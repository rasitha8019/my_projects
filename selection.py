def selection(list):
    for i in range(len(list)):
        min_index=i
        for j in range(i+1,len(list)):
            if list[j]<list[min_index]:
                min_index=j
        list[i],list[min_index]=list[min_index],list[i]
    return list
print(selection([5,7,4,3,8,6,1,9,2 ]))
