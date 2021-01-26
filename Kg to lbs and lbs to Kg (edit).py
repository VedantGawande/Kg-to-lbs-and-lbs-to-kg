q = ""
while q.lower() != "q": 
    print("\t\tWELCOME TO KG TO POUNDS AND POUNDS TO KG CONVERTER")

    name = input("What is your name? ")
    print(f"Hello {name}")

    print("---------------------------------------")

    invalid = True
    while invalid:
        try:
            weight = float(input("Please enter your weight: "))
            if weight < 10:
                print("You seem to be the lightest person on earth")
            elif weight > 200:
                print("You need to lose weight!")
            else:
                invalid = False
        except:
            print("Wrong input.")

    print("---------------------------------------")

    print("In which unit is your weight? ")
    invalid_2 = True
    while invalid_2:
        try:
            unit = int(input("For Kg type 1\nFor Lbs type 2: "))
            invalid_2 = False
            while ((unit != 1) and (unit != 2)):
                unit = int(input("Please enter 1 for Kg\nand 2 for Lbs: "))
        except:
            print("Wrong input.")
    
    print("---------------------------------------")
    
    if unit == 1:
        weight_lbs = weight * 2.2046226218
        print(f"{name}'s weight is: {weight_lbs} Lbs")
    elif unit == 2:
        weight_kg = weight / 2.2046226218
        print(f"{name}'s weight is: {weight_kg} Kg")
    else:
        print("Please use a valid unit...")

    q = input('If you want to quit press "Q" or press enter to convert again: ')

print("......................................")
print(f"Thank you {name}")
input("Press Enter ")