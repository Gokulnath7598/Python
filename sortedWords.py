fname = input("Enter file name: ")
fh = open(fname)
lst = []
bst = []
love = list()
for line in fh:
    b = line.strip()
    c = b.split(" ")
    lst.append(c)
for l in lst:
    bst = bst + l
for h in bst:
    love.append(h)
love.sort()
res = []
for i in love:
    if i not in res:
        res.append(i)
print(res)