arr=[1,2,3,4,5,6,7]

res1=arr[0]

for i in range(7):
    res1=res1^arr[i]

print(res1)

arr=[1,2,3,5,4,7]
res=arr[0]

for i in range(6):
    res=res^arr[i]

print(res)

print(res1^res)