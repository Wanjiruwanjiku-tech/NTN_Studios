# Mini Project 2: Expense Splitter
# Requirements
# 1. Ask for total bill amount
# 2. Ask how many people are splitting it
# 3. Calculate each person's share
# 4. Output with two decimal places
#  tip: Use round(amount, 2) for cleaner output

try:
    print("Need Help splitting the bill?")
    total_bill = float(input("Enter the Total bill to split: "))
    number_of_people = int(input("Enter the number of people: "))

    amount = total_bill / number_of_people
    bill_per_person = round(amount, 2)

    print(f"The Bill per person is: {bill_per_person}")
    print(f"Breakdown\n\tTotal Bill: {total_bill} ksh.\n\tNumber of People: {number_of_people}.\n\tEach Person: {bill_per_person} ksh.\nThank You\n")
except ValueError:
    print("Invalid input, use numbers only")