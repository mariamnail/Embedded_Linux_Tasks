from fav_websites import*

print("1- Google")
print("2- Facebook")
print("3- Twitter")
print("4- whatsapp")
print("5- GitHub")
x = input("Choose the website do you want:")

if x == '1':
    firefox(websites["Google"])
elif x == '2':
    firefox(websites["Facebook"])
elif x == '3':
    firefox(websites["Twitter"])
elif x == '4':
    firefox(websites["Whatsapp"])
elif x == '5':
    firefox(websites["GitHub"])
    


    