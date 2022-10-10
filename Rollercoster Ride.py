print("Welcome to Rollercoster Ride")
A = int(input("Enter Your Height :- "))
if A >= 120 :
    print("You Are Eligible to Ride !!!")
    B = int(input("Enter Your Age :- "))
    if B > 12 :
        print("You Fare is 5$")
    elif B <=18:
        print("You Fare is 7$")
    elif B >=18 :
        print("You Fare is 12$")
else:
    print("You Are Not Eligible to Ride")
