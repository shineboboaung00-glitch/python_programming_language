import random
import string
len = int(input("Enter the password len: "))
characters = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.choice(characters) for _ in range(len))
print("You password is :", password) 