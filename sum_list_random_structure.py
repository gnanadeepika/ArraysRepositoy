def sum_list(L):
    total=0
    for i in L:
        if isinstance(i,list):
            total=total+sum_list(i)
        else:
           total+=i
    return total

def sum_list_stack(L):
    total=0
    item = list(L)
    print(item)
    while item:
        first = item.pop(0)
        if isinstance(first,list):
            item.extend(first)
            print(item)
        else:
           total+=first
    return total



l=[1,2,[1,2,[1,3]]]
func = sum_list_stack
print(func(l))