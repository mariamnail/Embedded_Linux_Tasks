myname = ['Mariam' , 'Mohamed' , 'Abdel-Hamid' , 'Mohamed']
f = open("name.txt","w")
f.write(" ".join(myname))
f = open("name.txt","r")
print(f.read())