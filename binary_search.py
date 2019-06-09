a=[1,2,3,4,5]
ele=4
low=0
high=len(a)-1
mid=int((low+high)/2)
pos=-1
while(low<high):
    mid=int((low+high)/2)
    if(a[mid]==ele):
        pos=mid+1
    elif(a[mid]<ele):
        low=mid+1
    else:
        high=mid-1
if pos==-1:
    print("Number is not found")
else:
    print(ele,"is present at position",pos)
