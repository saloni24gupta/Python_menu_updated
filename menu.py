import os
os.system("tput setaf 3")
print("\t\t\tWelcome to MY MENU !!")
os.system("tput setaf 7")
print("\t\t\t-----------------")
#r = input("Where to want to run this menu ? (y/n) :")

#print(r)
print("""
\n
press 1 : to run date
press 2 : to cal
press 3 : to hadoop storage list
press 4 : to user create
press 5 : to ext
""")
 
ch = input("Enter ur choice : ")
print(ch)
if int(ch) == 1:
       os.system("date")

elif int(ch) == 2:
       os.system("cal")
else:
        os.system("exit")


