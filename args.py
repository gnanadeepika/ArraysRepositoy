def f(*args,**kwargs):
    print(args, kwargs)

l = [1,2,3]
t = (4,5,6)
d = {'a':7,'b':8,'c':9}

f(1,2,t)
f(1,2,*t,[d],6,7,8)
exit()
f(1,2,3)
f(1,2,3,"groovy")
f(a=1,b=2,c=3)
f(1,2,3,a=1,b=2,c=3)
f(*l,**d)
f(*t,**d)
f(1,2,t)
f(q="winning",**d)

