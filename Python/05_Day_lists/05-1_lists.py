empty_list = list()
print("This is an empty list: \"{}\"".format(empty_list))

fruits = ["apples", "banana", "oranges", "mango", "lemon", "peaches", "kiwi"]
print(f"A fruit list with more than five items: {fruits}")
print(f"The length of my List is: {len(fruits)}")
print(f"The first item is: {fruits[0]}\nThe middle item is: {fruits[len(fruits) // 2]}\nThe last item is: {fruits[len(fruits) - 1]}")
print('-' * 40)

mixed_data_types = ['Natalie', 28, 164.3, {'maritial status': 'single'}, '123 waithaka street']
print('This is a list with mixed data types: {}'.format(mixed_data_types))
print('-' * 40)

it_companies = ['Facebook', 'Google', 'Microsoft', 'IBM', 'Oracle', 'Amazon']
print("A list of I.T Companies: %s"%(it_companies))
print("The number of companies is: %d"%(len(it_companies)))
print(f"The first item is: {it_companies[0]}\nThe middle item is: {it_companies[len(it_companies) // 2]}\nThe last item is: {it_companies[len(it_companies) - 1]}")

it_companies.append('NTN Studios')
print("Appended a new company: {}".format(it_companies))

it_companies.insert(0, 'Jojos')
print("inserter a new company at index 0: {}".format(it_companies))

it_company = it_companies[2]
upper_case = it_company.upper()
it_companies[2] = upper_case
print("Changed index 2 \"Google\" to uppercase: {}".format(it_companies))

it_companies.extend('#')
print(it_companies)
print(f"Reversed list using slicing: {it_companies[::-1]}")

it_companies.reverse()
print(f"Reversed list using reverse method: {it_companies}")