arr=[3,3,4,3,4,4,2,4,4]

def majority_element(arr):
    count=0
    element = arr[0]
    for i in range(len(arr)):
        if element == arr[i]:
            count = count +1
        if element != arr[i]:
            count = count -1
        if count ==0:
            element = arr[i]
            count=1
    print("Element is ",element)
    return element

def count_element(element,arr):
    count=0
    for i in range(len(arr)):
        if element== arr[i]:
            count = count+1
    print("Count is ",count)
    if count > len(arr)//2:
        return element
    else:
        return "No element"

#print(count_element(4,arr))
print(count_element(majority_element(arr),arr))