a = input("Please enter Bit 0 mode:")
b = input("Please enter Bit 1 mode:")
c = input("Please enter Bit 2 mode:")
d = input("Please enter Bit 3 mode:")
e = input("Please enter Bit 4 mode:")
f = input("Please enter Bit 5 mode:")
g = input("Please enter Bit 6 mode:")
h = input("Please enter Bit 7 mode:")

if a.lower() == "in":
    i=0
elif a.lower() == "out":
    i=1

if b.lower() == "in":
    j=0
elif b.lower() == "out":
    j=1
     
if c.lower() == "in":
    k=0
elif c.lower() == "out":
    k=1
    
if d.lower() == "in":
    l=0
elif d.lower() == "out":
    l=1    

if e.lower() == "in":
    m=0
elif e.lower() == "out":
    m=1
    
if f.lower() == "in":
    n=0
elif f.lower() == "out":
    n=1
    
if g.lower() == "in":
    p=0
elif g.lower() == "out":
    p=1
       
if h.lower() == "in":
    q=0
elif h.lower() == "out":
    q=1
                    
f = open("init.c","w")
f.write("\nvoid Init_PORTA_DIR(void){\n")
f.write(f"    DDRA = 0b{q}{p}{n}{m}{l}{k}{j}{i};\n")
f.write("}")
f = open("init.c","r")
print(f.read())

