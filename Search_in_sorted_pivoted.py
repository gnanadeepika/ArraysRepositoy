def binary_search(arr,item,start,end):
    mid=round((end+start)/2)
    if arr[mid] < item:
       return binary_search(arr,item,mid+1,end)
    elif arr[mid] > item:
       return binary_search(arr,item,start,mid-1)
    elif arr[mid]==item:
       return mid
    else:
        return "notfound"

arr=[4,5,1,2,3]
item=5
if arr[0]==1:
    binary_search(arr,item,0,len(arr)-1)
else:
    break_point=(5-arr[0])+1
    print(break_point)
    if item <= (5-break_point):
        start=break_point
        end=len(arr)-2
        print(start,end)
        print("output",binary_search(arr,item,start,end))
    else:
        start=0
        end=break_point-1
        print(start,end)
        print("output",binary_search(arr,item,start,end))