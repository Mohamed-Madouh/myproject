from optparse import Option
from turtle import update


admins= ["Ahmed","Osama","Sameh","Manal","Rahma","Mohamed","Enas"]
name=input("please type you Name ").capitalize().strip()
if name in admins:
    print (f"Hello {name} Welcome Back")

    options = input("Delete Or Update Your Name ?").capitalize().strip()
    if options == 'Update'or options == 'U':
        TheNewName= input("Entar The New Name ").capitalize().strip()
        admins[admins.index(name)]= TheNewName
        print ("Name Updated.")

    elif options == 'Delete'or options=='D':
        admins.remove(name)
        print ("Name Deleted.")
    else:
        print ("Wrong option Choosed")

else:
    status = input ("Not Admin, Add You Yes or No ?")
    if status == 'Yes' or status == 'Y':
        print ("You Have Been Added")
        admins.append(name)
        print (admins)
    else:
        print("You  Are Not Admin.")

