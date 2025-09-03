first_set = {1, 2, 3}
second_set = {3, 4, 5}
print(f"The first set is: {first_set}")
print(f"The second set is: {second_set}")
print("-" * 40)

union_set = first_set.union(second_set)
print(f"union_set = {union_set}")

intersection_set = first_set.intersection(second_set)
print(f"intersection_set = {intersection_set}")

difference_set = first_set.difference(second_set)
print(f"difference_set = {difference_set}")
print("-" * 40)

# mini-project
my_fruits = {"apples", "bananas", "mangoes"}
friends_fruits = {"peaches", "oranges", "mangoes"}

print(f"My favorite fruits include: {my_fruits}")
print(f"My friend's favorite fruits include: {friends_fruits}")

intersection_fruit = my_fruits.intersection(friends_fruits)
print(f"We both like: {intersection_fruit}")

difference_a = my_fruits.difference(friends_fruits)
difference_b = friends_fruits.difference(my_fruits)

print(f"My special preference is: {difference_a}")
print(f"My friend's special preference is: {difference_b}")