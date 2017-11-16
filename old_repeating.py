arr=[1,2,1,2,3,1,2,3,1,2,4,4,6]
op=arr[0]
for i in range(1,len(arr)):
    op=op^arr[i]
print(op)