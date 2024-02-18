# Today we are learing about if and else statments

#  the % gives a remainder like 7 % 2 it will print out 1
print("welcome to the rollercoster! ")
height = int(input("what is your height in cm? "))

bill = 0

if height >= 120:
    print("you can ride the rollercoster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("child tickets are $5.")
        bill = 5
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age <= 44:
        bill = 12
        print("Adult tickets are $12.")
    elif not age >= 45  <= 55:
        print("your ticket is on us! Enjoy the ride.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3
    
    print(f"Your final bill is ${bill}")



else:
    print("Sorry, you cant ride the rollercoster...")

# the \ helps it ignore the ' for the string
print('You\'re at a cross roads do you want to go "left" or "right".')

