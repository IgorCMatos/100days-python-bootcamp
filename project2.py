print("Welcome to the tip calculator")
bill = float(input("How much was the bill? "))
tip = float(input("How much tip would you like to give? in percentage: "))
people = int(input("How many people to slit the bill? "))

tip_amount = (bill * tip) / 100
total_bill = bill + tip_amount
each_pay = total_bill / people

print(f"Each one will pay {each_pay:.2f}")
