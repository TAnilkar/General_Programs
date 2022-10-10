print("Welcome to BMI calculator")
A = float(input("Enter your Height in Foot : "))
B = int(input("Enter your Weight : "))
C = float(A) * float(0.3048)
BMI = float(B) / int(C ** 2)
print(f"Your BMI is : {BMI}")

if float(BMI) <= 18.5:
    print("You Are UnnderWeight!!!")
elif float(BMI) <= 25:
    print("You Are Normal!!!")
elif float(BMI) <= 30:
    print("You Are OverWeight!!!")
elif float(BMI) >= 30:
    print("You Are Obese!!!")
