Bill = int(input("Enter Your Total Bill :- "))
Z = int(input("Enter tip you want to add in Percentage of total bill (10 , 20 , 50 ,100, etc.) :- "))
A = Z/int(100)
B = int(Bill) * A
Tip = int(Bill) + int(B)

D = int(input("Enter bill should split into peoples :- "))
C = int(Tip) / int(D)
print(f"Each Should Pay :- {C}")