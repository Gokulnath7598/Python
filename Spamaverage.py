# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
result = 0.0
count = 0
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    index = line.find(":")
    val = line[index+1:].strip()
    count = count+1
    result = result + float(val)
print("Average spam confidence:",result/count)
