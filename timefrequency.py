name = input("Enter file:")
handle = open(name)
a = list()
lst = dict()
for line in handle:
    l = line.strip()
    if not l.startswith("From "):
        continue
    m = l.split(" ")
    n = m[6].split(":")
    a.append(n[0])
for ab in a:
    lst[ab] = lst.get(ab, 0) + 1
for k,v in sorted(lst.items()):
    print(k,v)