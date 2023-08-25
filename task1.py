f = open("doc.txt","w")
f.write("mariam\nmohamed\nabdelhamid\nmohamed")
f.close()
f = open(r"doc.txt",'r')
print(f.read())
with open(r"doc.txt",'r') as f:
    lines = f.readlines()
    print(len(lines))
f.close()