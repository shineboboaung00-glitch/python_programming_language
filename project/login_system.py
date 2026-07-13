user_name = input("Create the Username: ")
user_pass = input("Create the Userpassword: ")

print("Sucressful account create.")

super_user = input("Enter the Username: ")
super_user_pass = input("Enter the Password: ")

if user_name == super_user and user_pass == super_user_pass :
    print(f"Welcome {user_name}")
elif user_name == super_user:
    if user_pass == super_user_pass:
        print("Password Right")
    else:
        print("Password worng")
else:
    print("User Name is Wrong")