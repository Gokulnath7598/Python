name = input("Enter file:")
handle = open(name)
a = list()
lst = dict()
for line in handle:
    l = line.strip()
    if not l.startswith("From:"):
        continue
    m = l.split(" ")
    a.append(m[1])
for ab in a:
    lst[ab] = lst.get(ab,0)+1
bname = None
bcount = None
for name,count in lst.items():
    if bname is None or count > bcount:
        bname = name
        bcount = count
print(bname,bcount)
    
    