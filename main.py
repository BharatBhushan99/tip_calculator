print("Welcome to the tip calculator.")
amount = float(input("What was the total bill? $"))
tip = int(input(f"What percentage of tip would you like to give? 10, {9+3}, or 15? "))
total = amount + amount * (tip /100)
people = int(input("How many people to split the bill? "))
payment = round(total/people, 2)
print("Each person should pay: ${:.2f}".format(payment))
  