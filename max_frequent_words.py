dataarr=[]
try:
    with open("data.txt",'r') as f:
        for line in f.readlines():
            line=line.rstrip("\n")
            for i in line.split(" "):
                dataarr.append(i.lower())
except:
    print("Could open file")

print(dataarr)
words=[]
for i in dataarr:
    if i not in words:
        words.append(i)

print(words)
countarr=[]
for i in words:
    countarr.append((i,dataarr.count(i)))

print(countarr)