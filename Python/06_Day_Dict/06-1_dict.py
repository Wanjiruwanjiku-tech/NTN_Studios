# 1. Create an empty dict called dog
dog = dict()
print('-' * 40)
print(f'This is an empty dog dictionary:{dog}')

# 2. Add name, color, breed, legs, age to the dog dict
dog['name'] = 'Bud'
dog['color'] = 'Black'
dog['breed'] = 'African hound'
dog['legs'] = 4
dog['age'] = 5

print(f'Meet my dog:{dog}')
print('-' * 40)

# 3. Create a student dictionary.

student = {
    'first_name': 'Natalie',
    'last_name': 'Wanjiru',
    'gende': 'female',
    'age': 28,
    'maritial_status': 'single',
    'skills': ['programming', 'paramedic', 'graphics', 'animator',],
    'country': 'Kenya',
    'city': 'Nairobi',
    'address': {'street': 'Waithaka', 'zip': '2546'}
}
print(f'These are my student\'s details: {student}')
print(f'\nThe length of my dictionary is: {len(student)}')
print(f'\nThese are my student\'s skills: {student["skills"]}')

student['hobbies'] = ('coding', 'gaming', 'writing')
print(f'\nAdded new item to the list: {student.get("hobbies")}')

student_keys = student.keys()
print("\nThese are all the keys found in student dictionary:{}".format(student_keys))
student_values = student.values()
print("\nThese are all the values found in student dictionary:{}".format(student_values))

student_tuple = student.items()
print(f"\nTurned dict to tuple: {student_tuple}")

student.pop('address')
print("\nDeleted student address: {}".format(student))

student.popitem()
print("\nDeleted last item: {}".format(student))

student.clear()
print("\nCleared student dict: {}".format(student))
