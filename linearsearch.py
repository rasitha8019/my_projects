def linearSearch(list,number):
    for i in list:
        if i==number:
            return True
    return False
print(linearSearch([5,9,3,1,2,8,4,7,6],17))