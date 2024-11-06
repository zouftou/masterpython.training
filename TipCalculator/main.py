print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = float(input("How much tip whould you like to give?"))
people = int(input("How many people to split the bill?"))
tip_percentage = tip / 100
bill_with_tip = bill * (1 + tip_percentage)
total = bill_with_tip / people
print(f"Each person should pay: ${round(total,2)}")