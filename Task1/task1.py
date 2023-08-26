f = open("doc.txt","w")
f.write("mariam\nmohamed\nabdelhamid\nmohamed")
f = open(r"doc.txt",'r')
file = f.read()
print(file)
with open("doc.txt",'r') as f:
    lines = len(f.readlines())
    print("no. of lines:" ,lines)
    print("no. of words:" ,len(file.split()))