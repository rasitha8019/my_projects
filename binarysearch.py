import math
def binarysearch(list,value):
    start=0
    end=len(list)-1
    while start<=end:
        mid=math.floor((start+end)/2)
        if list[mid]==value:
            return True
        elif value<list[mid]:
            end=mid-1
        else:
            start=mid+1
    return False   
print(binarysearch([1,2,3,4,5,6],14))
