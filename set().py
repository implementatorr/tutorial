numbers = {14, 8, 56, 29, 47, 39, 97, 180, 145}
print(14 in numbers)

fruits = {"Mango", "Apple", "Banana", "Strawberry"}
fruits.add('Orange')
print(fruits)

fruits = {"Mango", "Apple", "Banana", "Strawberry"}
numbers = {14, 8, 56, 29, 47, 39, 97, 180, 145}
new_set = fruits.union(numbers)
print(new_set)

fruits1 = {"Mango", "Apple", "Banana"}
numbers1 = {14, 8, 56, 29, 97, 180, 145}
fruits1.update(numbers1)
print(fruits1)

fruits = {"Mango", "Apple", "Banana", "Strawberry"}
fruits.remove('Mango') or fruits.discard('mango')
print(fruits)


fruits = {"Mango", "Apple", "Banana", "Strawberry"}
fruits.discard('Mang')
print(fruits)


fruits = {"Mango", "Apple", "Banana", "Strawberry"}
fruits.pop()
print(fruits)


fruits = {"Mango", "Apple", "Banana", "Strawberry"}
fruits.clear()
print(fruits)

# The del keyword is used to delete the set completely
fruits = {"Mango", "Apple", "Banana", "Strawberry"}
del fruits
print(fruits)  # This will raise an error because the

# The copy() method is used to copy the set
fruits = {"Mango", "Apple", "Banana", "Strawberry"}
new_set = fruits.copy()
print(new_set)

# The difference() method returns a set that contains the difference
# between two sets
fruits = {"Mango", "Apple", "Banana", "Strawberry"}
companies = {"Google", "Microsoft", "Apple"}
# The returned set contains items that exist only in the first set,
# and not in both sets
diff_set = fruits.difference(companies)
print(diff_set)

# The difference_update() method remove the the items that exist in
# both sets
fruits = {"Mango", "Apple", "Banana", "Strawberry"}
companies = {"Google", "Microsoft", "Apple"}
fruits.difference_update(companies)
print(fruits)

# The intersection() method returns a set that contains the similarity
# between two or more sets
fruits = {"Mango", "Apple", "Banana", "Strawberry"}
companies = {"Google", "Microsoft", "Apple"}
# The returned set contains only items that exist in both sets, or in
# all sets if the comparison is done with more than two sets
intersect_set = fruits.intersection(companies)
print(intersect_set)

# The intersection_update() method removes the items that is not
# present in both sets
fruits = {"Mango", "Apple", "Banana", "Strawberry"}
companies = {"Google", "Microsoft", "Apple"}
fruits.intersection_update(companies)
print(fruits)

# The isdisjoint() method returns True if none of the items are
# present in both sets, otherwise it returns False
# fruits = {"Mango", "Apple", "Banana", "Strawberry"}
companies = {"Google", "Microsoft", "Android"}
check_sets = fruits.isdisjoint(companies)
print(check_sets)

# The issubset() method returns True if all items in the set exists in
# the specified set, otherwise it returns False
fruits = {"Mango", "Apple", "Banana", "Strawberry"}
fruits_set = {"Apple", "Banana"}
check_set = fruits.issubset(fruits_set)
print(check_set)

# The issuperset() method returns True if all items in the specified
# set exists in the original set, otherwise it returns False
fruits = {"Mango", "Apple", "Banana", "Strawberry"}
fruits_set = {"Apple", "Banana"}
check_set = fruits.issuperset(fruits_set)
print(check_set)

# The issuperset() method returns True if all items in the specified
# set exists in the original set, otherwise it returns False
fruits = {"Mango", "Apple", "Banana", "Strawberry"}
fruits_set = {"Apple", "Banana"}
check_set = fruits.issubset(fruits_set)
print(check_set)

# The symmetric_difference() method returns a set that contains all
# items from both set, but not the items that are present in both sets
fruits = {"Mango", "Apple", "Banana", "Strawberry"}
companies = {"Google", "Microsoft", "Apple"}
new_set1 = fruits.symmetric_difference(companies)
print(new_set1)

##The symmetric_difference_update() method updates the original set by
# removing items that are present in both sets, and inserting the other
# items
fruits = {"Mango", "Banana", "Strawberry", "Orange"}
fruits_set = {"Apple", "Orange", }
fruits.symmetric_difference_update(fruits_set)
print(fruits)