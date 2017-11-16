ip=900002

mapping={1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen",20:"twenty",30:"thirty",40:"fourty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety",100:"hundred",1000:"thousand",10000:"lakh"}

def get_tens(ip):
    if ip <= 20:
        return mapping[ip]
    else:
        if ip%10 != 0:
            return mapping[(ip//10)*10]+" "+mapping[ip%10]
        else:
            return mapping[(ip//10)*10]

def get_hundreds(ip):
    print("hundred",ip//100,ip%100)
    if ip%100 ==0:
        return mapping[ip//100]+" "+mapping[100]
    if ip//100 != 0:
        return mapping[ip//100]+" "+mapping[100]+" "+get_tens(ip%100)
    else:
        return get_tens(ip%100)


def get_thousands(ip):
    print("Thousands :",ip//1000,ip%1000)
    if ip%1000 ==0:
        return get_tens(ip//1000)+" "+mapping[1000]
    if ip==0 : return get_hundreds(ip%1000)
    if ip//1000 !=0:
        return get_tens(ip//1000)+" "+mapping[1000]+" "+get_hundreds(ip%1000)
    else:
        get_hundreds(ip%1000)


def get_lakhs(ip):
    print("Lakhs :",ip//100000,ip%100000)
    if ip%100000 == 0:
        return  get_tens(ip//100000)+" "+mapping[10000]
    return get_tens(ip//100000)+" "+mapping[10000]+" "+get_thousands(ip%100000)

#print(get_lakhs(ip))

if ip < 100:print(get_tens(ip))
elif ip < 1000 : print(get_hundreds(ip))
elif ip < 100000: print(get_thousands(ip))
else: print(get_lakhs(ip))




