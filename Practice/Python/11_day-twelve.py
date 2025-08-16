word = "Python"
count = 1
for letter in word:
    print (f"\t{letter}")

while count <= 10:
    print (count)
    count += 1

    if count == 5:
        continue
    elif count == 7:
        break
print("Blast Off!!")