while True:
    user_grade = int(input("Enter the source: "))

    if user_grade >=40 and user_grade <=60:
        print("You Grade C")
    elif user_grade >=61 and user_grade <= 80:
        print ("You Grade is B") 
    elif user_grade >=81 and user_grade <=90:
        print ("Your Grade is A")
    elif user_grade >=91 and user_grade <=100:
        print ("You Grade is A+")
    else :
        print("Fail")