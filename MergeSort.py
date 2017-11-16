def merge(l1,l2):
    i=0;j=0;l=[]
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            l.append(l1[i])
            i=i+1
        elif l1[i] > l2[j]:
            l.append(l2[j])
            j=j+1
    while(i < len(l1) ):
        l.append(l1[i])
        i=i+1
    while(j < len(l2) ):
        l.append(l2[j])
        j=j+1
    return l



def mergesort(arr,start,end):
    prinr(a)
    if start < end:
        if len(arr)==1:
            return arr
        if len(arr)>2:
            mid=round((len(arr)-1)/2)
        else:
            mid=1
        l1=mergesort(arr,start,mid)
        l2=mergesort(arr,mid+1,end)
        #merge(l1,l2)


arr=[14,22,27,10,35,19,42,44,2]
print(mergesort(arr,0,len(arr)-1))
#print(merge([1],[11,16,61,94]))