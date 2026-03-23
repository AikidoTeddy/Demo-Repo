
age = int(input("Enter your age: "))
DOTW = input("Enter the day of the week: ")
membership_status = input("Are you a  member: ")

if age<0:
   print("An error message")
elif age<13:
   
   price =7
   
elif age>=65:
   
   price=9
   
else:
   price=12    
if DOTW=="wednesday":
   price=price-2
if membership_status=="yes":
   price=price-0.10
   

print("your ticket will be",price)   

      




    
