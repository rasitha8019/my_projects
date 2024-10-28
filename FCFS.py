n=int(input("enter no of jobs"))
dict={}

for i in range(n):
    list=[]
    x=int(input(f"enter At of {i+1}"))
    y=int(input(f"enter BT of {i+1}"))
    list.append(x)
    list.append(y)
    key="P"+str(i+1)
    dict[key]=list
at=sorted(dict.items(),key=lambda item:item[1][0])
ct=len(at)
sum=0
ct={}
for i in range(len(at)):
        if(i==0):
            sum=sum+at[i][1][1]
        if(at[i][1][0]<=sum):
            sum=sum+at[i][1][1]
        elif(at[i][1][0]>sum):
            sum=sum+(at[i][1][0]-sum)
            sum=sum+at[i][1][1]
        ct[at[i][0]]=sum
tat={}
ta=0
for i in range(len(at)):
     t=ct[at[i][0]]-at[i][1][0]
     tat[at[i][0]]=t
     ta=ta+t
print(f"TAT average ={ta/n}")
wt={}
b=0
for i in range(len(at)):
     x=tat[at[i][0]]-at[i][1][1]
     wt[at[i][0]]=x
     b=b+x
print(f"WT average={b/n}")


     

     

   




    