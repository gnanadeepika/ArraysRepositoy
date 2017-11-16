a=[1,2,3,4,5,6]
b=[]
p=int(input("Enter a pivot: "))
print(p)

b.extend(a[p:])
b.extend(a[0:p])

print(b)
