l=[11,14,30,39,42,50]
sum=91

def check_sum(l,sum):
    min=0
    max=len(l)-1
    while min < max:
        if l[min]+l[max]==sum:
            return True
        elif l[min]+l[max]>sum:
            max=max-1
        elif l[min]+l[max]<sum:
            min=min+1
    return False

print("output is ===",check_sum(l,sum))