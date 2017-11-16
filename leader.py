arr=[16, 17, 4, 3, 5, 2]
leader=[]

for i in range(1,len(arr)-1):
    if (arr[i]> arr[i-1]) and (arr[i]>arr[i+1]):
        leader.append(arr[i])
leader.append(arr[i+1])
print(leader)