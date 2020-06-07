fname = input("Enter file name: ")
fr=open(fname)
b = []
count = 0
for line in fr:
    l = line.strip()
    if l.startswith("From:"):
        b = l.split(" ")
        print(b[1])
        count += 1
print("There were",count,"lines in the file with From as the first word")