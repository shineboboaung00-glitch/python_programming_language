do_to = []



def show():
    return(do_to)

def add():
    user_input = input("Enter the Task: ")
    do_to.append(user_input)
    print(f"{user_input} is add Sucressful")


def remove():
    user_input = input("Enter the remove Task: ")
    do_to.remove(user_input)
    print(f"{user_input} is remove Sucressful")

print ("1.show 2.add 3.remove 4.exit")


while True:
        user = input("Choice the number: ")
        if user == "1":
            show()
        elif user == "2":
            add()
        elif user == "3":
            remove()
        elif user == "4":
            print("Thanks You For Us")
            break