do_to = []

def show_do_to():
    print(do_to)

def add_do_to():
    while True:
        user_input = input("Add the task: ")
        super_user = user_input.capitalize()
        if super_user == "Exit":
            break
        else:
            do_to.append(super_user)
            print(f"{super_user} add is sucressful.")

def remove_do_to():
    
    while True:
        user_input = input("Remove the task: ")
        super_user = user_input.capitalize()
        if super_user == "Exit":
            break
        else:
            do_to.remove(super_user)
            print(f"{super_user} remove is sucressful.")

def exit():
    print("Thanks You For Us")
    

while True:
    print("1.show 2.add 3.remove 4.exit")
    user_choice = input("Choice the number: ")
    
    if user_choice == "1":
        show_do_to()
    elif user_choice == "2":
        add_do_to()
    elif user_choice == "3":
        remove_do_to()
    elif user_choice == "4":
        exit()
    else:
        print("Something is wrong.")