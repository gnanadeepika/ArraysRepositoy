def binary_search(arr,item,start,end):
    mid=round((end+start)/2)
    if arr[mid] < item:
       return binary_search(arr,item,mid+1,end)
    elif arr[mid] > item:
       return binary_search(arr,item,start,mid-1)
    elif arr[mid]==item:
       return mid



arr=[1,2,3,5,12,16]
item=12
print(binary_search(arr,item,0,5))