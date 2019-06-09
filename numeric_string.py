s1='1234'
count=0
for i in s1: 
    if(i.isnumeric())==True: 
        count+=1
if count==len(s1):
    print("S1 is numeric")
else:
    print("S1 is not numeric")
    
count=0
s2='1df4'
for i in s2:
    if(i.isnumeric())==True: 
        count+=1
if count==len(s2)-1:
    print("S2 is numeric")
else:
    print("S2 is not numeric")

