input="abab"

substrings=[]
op=[]
for i in range(len(input)):
    substrings.append(input[i])

for i in range(len(input)):
    for j in range(i+1,len(input)+1):
        substrings.append(input[i:j])


for i in substrings:
    if i not in op:
        op.append(i)

print(op)