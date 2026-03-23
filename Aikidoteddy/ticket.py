name=input("enter your name:  ")
print("hello " ,name, "welocme to PVPmovies")
age=int(input("enter your age: " ))
day=input("enter the day: ")
member=input("are you a member of pvp movies: ")
if age < 0:
    print("Invalid Age")
elif age < 13:
    price = 7
elif age >= 65:
    price = 9
else:
    price = 12

if day == "wednesday":
    price=price-2

if member =='yes':
    price=price-0.10

print("your final price will be:$",price ,name)

