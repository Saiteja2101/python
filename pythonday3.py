Direction = input("Welcome to the Treasure Island\nWhich direction do you want to choose if left type l or if type r ")
if Direction == "l":
    print("congratulations! now you are in the second round! ")
    Choise = input("do you want to swim if yes type y or type n ")
    if Choise == "n":
        print("congratulations! now you are in the third round! ")
        Door = input("Which door you want to select? if red type r or if yellow type y or type b ")
        if Door == "y":
            print("congratulations! you have won! ")
        elif Door == "r" or "b" :
            print("Sorry You lost ")
    elif Choise == "y":
        print("Sorry You lost ")
else:
    print("Sorry You lost ")