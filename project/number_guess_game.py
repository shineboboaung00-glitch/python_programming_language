import random
number = random.randint(1, 100)
guess = None
print(number)
while guess != number:
    guess = int(input("Enter the number 1 to 100 : "))
    if guess < number:
        print("number is low")
    elif guess > number:
        print("number is high")
    else:
        print("You win")