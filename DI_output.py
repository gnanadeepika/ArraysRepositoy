n=int(input("Enter a value :"))
str=input("Enter combo of D and I less then N-1 :")
a=[]
for i in range(n):
    a.append(i+1)
for i in str:
    if i == 'D':
        print(a.pop(),end=",")
    elif i=='I':
        print(a.pop(0),end=",")
print(a.pop())
