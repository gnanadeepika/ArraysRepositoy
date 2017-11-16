arr=[1,2,4,5,7,3,8]

def searchsum(x,arr):
    for i in range(len(arr)):
        element= x-arr[i]
        if element in arr[:]:
            print(element,arr[i])




searchsum(10,arr)