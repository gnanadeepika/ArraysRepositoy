l=[3,4,7,1,2,9,8]
dict={}

for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        sum=l[i]+l[j]
        if sum in dict.keys():
            print(dict[sum],(l[i],l[j]))
        else:
            dict[sum]=(l[i],l[j])
