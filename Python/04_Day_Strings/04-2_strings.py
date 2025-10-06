company = 'Coding for All.'
print('{}'.format(company))
print("Let's experiment with the string above\n")

print(f'First character: {company[0]}')
print(f'Title cased: {company.title()}')
print('Swap case: {}'.format(company.swapcase()))
word_check = company.find("Coding")
substring = 'for'
word_check_2 = company.index(substring)
print(f"Find the word \"Coding\": {word_check}")
print(f"Second word check for \"for\": {word_check_2}")

print(f"Replace the word \"Coding\": {company.replace('Coding', 'Python')}")
print(f"Split using space: {company.split(' ')}")

socials = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(f"Split the string \"{socials}\" at the comma: {socials.split(',')}")

print(f"Print the character at index 0: {company[0]}")
print(f"Print the character at index 10: {company[10]}")

phrase = "Python For Everyone"
print("Abbreviation fo the phrase \"{}\" is: {}".format(phrase, phrase[0: :2]))

print(f'First occurrence of the character \'C\' is at index: {company.index("C")}')
print(f'First occurrence of the character \'f\' is at index: {company.index("f")}')

new_company = 'Coding for all people'
print(f'Last occurrence of the character \'l\' in the Phrase \'{new_company}\' is at index: {new_company.rfind("l")}')

sentence = 'You cannot end a sentence with because because because is a conjunction'
print(f"\nNew sentence: {sentence}")
print(f"First occurrence of \"because\" is at index: {sentence.find('because')}")
print(f"Last occurrence of \"because\" is at index: {sentence.rindex('because')}")

print(f'Slice out the becauses: {sentence[31:54].split(" ")}')
print(f'Does the phrase start with "You": {sentence.startswith("You")}')
print(f'Does the phrase start with "end": {sentence.startswith("end")}')
print(f'Does the phrase end with "conjunction": {sentence.endswith("conjunction")}')
print(f'Does the phrase end with "because": {sentence.endswith("because")}')