
do_to = []

while True:
    print ("Choice the Number")
    print ("1.show 2.add 3.remove 4.exit")

    super_user = input("Enter the choice number: ")

    if super_user == "1":
        print(do_to)
    elif super_user == "2":
        user = input("Enter the add: ")
        do_to.append(user)
        print(f"{user} Sucressful is add.")
    elif super_user == "3":
        user = input("Enter the remove: ")
        do_to.remove(user)
        print(f"{user} sucressful is remove.")
    elif super_user == "4":
        print("Thanks you for us")
    else:
        print("Something is worng")
        break