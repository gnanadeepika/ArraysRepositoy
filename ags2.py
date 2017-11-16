def f2(**k):
    print(*k)
l = [1,2,3]
t = (4,5,6)
d = {'a':7,'b':8,'c':9}


#f2(1,2,3,'a') # (1,2,3,'a')
#f2(1,2,3,"groovy") # (1,2,3,"groovy")
f2(a=1,b=2,c=3) # error
#f2(arg1=1,arg2=2,c=3,zzz="hi") #error
#f2(1,2,3,a=1,b=2,c=3) #error

#f2(*l,3,**d) #error
#f2(*t,**d) #error
#f2(1,2,*t)
#f2(1,1,2,4,q="winning") # 1,1,2,4 {'q'="winning"}
#f2(1,2,*t,q="winning",**d) #error
