def sq_generator(l):
    for i in l:
        yield i*i

def scramble(l):
    for i in range(len(l)):
        l=l[-1]+l[:-1]
        yield l

def scramble2(l):
    for i in range(len(l)):
        yield l[i:]+l[:i]

def permute2(seq):
    if not seq:
        yield seq
    else:
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:]
            for x in permute2(rest):
                yield seq[i:i+1] + x



#op = sq_generator([1,2,3,4,5])

op=scramble2('spam')
op1=permute2('spa')

print(list(op))
for i in op1:
    print(i)