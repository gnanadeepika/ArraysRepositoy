def max_sum(L):
    return "" if not L else L[0]+max_sum(L[1:])

def master(master_name):
    def slave(slave_name):
        print(master_name+"===="+slave_name)
    return slave

def Outer(Name1):
    f = lambda x:print(x)
    return f


L = [lambda x:x**2,
     lambda x:x**3,
     lambda x:x**4]

for f in L:
    print(f(2))



m = master("IamMaster")
m("IamSlave")

o = master("IamOuter")
o("IamInner")

print(L[0](2))

#print(max_sum(["dee","pika"]))
