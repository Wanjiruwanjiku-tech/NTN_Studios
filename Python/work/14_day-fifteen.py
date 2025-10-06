students = ["Alice", "Natalie", "Ben", "Cathy"]
grades = [85, 79, 90, 65]

# Find the average grade
average = sum(grades) / len(grades)
print(f"Class average: {average}")

# Use list comprehension with a codition
passed = [students[i] for i in range(len(grades)) if grades[i] >= 70]
print(f"Passed: {passed}")

# Grade report
report = [f"{students[i]}: {grades[i]}" for i in range(len(students))]
print(report)