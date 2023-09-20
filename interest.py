#Algorithm to calculate interest
principal = float(input("Enter your principal (in currency): "))
rate = float(input("Enter your intrest rate (%): "))
time = float(input("Enter your in time period (in months): "))

simple_interest = (principal * rate * time) / 365

print("simple interest:", simple_interest)