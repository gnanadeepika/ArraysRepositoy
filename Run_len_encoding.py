input_string="wwwwbbbaaabbababds"
output="w"
cur=input_string[0]
count=1
for i in input_string[1:]:
    if i == cur:
        count+=1
    if i != cur:
        output+=str(count)
        cur=i
        output+=cur
        count=1
output+=str(count)

print(output)