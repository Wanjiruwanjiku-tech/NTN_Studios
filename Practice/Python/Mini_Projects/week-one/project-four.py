# Mini Project 4: Simple Interest Calculator
# Goal: Calculate the intrest over time.
# Requirements:
# 1. Ask for principal amount, rate (in %), and time (in years)
# 2. Use the formula: interest = (principal * rate * time) / 100
# 3. Print the calculated interest

principal_amount = float(input("Enter the Principal Amount: "))
rate = float(input("Enter the Intrest rate (in %): "))
time = int(input("Enter the time (in years): "))

interest = (principal_amount * rate * time) / 100
rounded_off_interest = round(interest, 2)

print(f"Simple Interest is:{rounded_off_interest}\n")
print("Breakdown:")
print(f"\tPrincipal: {principal_amount}ksh")
print(f"\tRate: {rate}%")
print(f"\tTime: {time} years")
print(f"\tInterest: {rounded_off_interest}ksh\n")