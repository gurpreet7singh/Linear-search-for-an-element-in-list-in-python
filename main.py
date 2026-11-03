l=[8,1,2,3,5,4,6,4,6]
elm=(int(input("Enter the element to be searched:")))
flag=0
n=len(l)
if elm in l:
    posi=l.index(elm)
    print(posi)
for i in range(0,n-1):
    if l[i]==elm:
        flag=flag+1
        break
if flag==1:
    print("Element found, and its possition is", (posi+1))
else:
    print("Element is not there")
