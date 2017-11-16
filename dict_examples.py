my_dict={'blue':1,'red':2,'yellow':3,'green':4}

print("Before deletion:",my_dict)

del_keys=[]

for k,v in [(k,v) for k,v in my_dict.items()]:
    if v>3:
        del my_dict[k]


#for k,v in my_dict.items():
#    if v > 3:
#        del_keys.append(k)

#for k in del_keys:
#    del my_dict[k]

print("after deletion:",my_dict)