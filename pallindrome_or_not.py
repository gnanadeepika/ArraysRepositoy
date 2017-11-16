l=[1,1,1,1]

i=0;
n=len(l)
n=n-1
flag=0
while i<=len(l)//2:
    if l[i]!=l[n-i]:
        flag=1
        break
    i=i+1

if(flag==1):
    print("not palindrome")
else:
    print("palindorme")