a=[[1,2,3,4],
   [5,6,7,8],
   [9,10,11,12],
   [13,14,15,16]]

for i in range(1,4):
    for j in range(0,i):
        print(i,j,sep="==")
        temp=a[i][j]
        a[i][j]=a[j][i]
        a[j][i]= temp


print(a)