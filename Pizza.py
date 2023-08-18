print("Welcome to Python Pizza Deliveries")

size = input("What size pizza do you want S, M , or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
want_drink = input("Do you want drink C or B and W ")
want_toy = input("Do you want to toy Y or N ")
seat_baby = input("Would you like a baby seat ")

# Options

bill = 0

if size == "S":
    bill += 15
    
elif size == "M":
    bill += 20
    
else:
    bill += 30

if add_pepperoni == "Y":
    if size == "S":
        bill +=5
else:
    bill += 3

if extra_cheese == "Y":
    bill += 5
if want_drink == "C or B and W":
    bill +=10
if want_toy == "Y":
    bill +=12 
if seat_baby == "Y":
    bill +=15 
    

print(f"Your finall bill is ${bill}")
