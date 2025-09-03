# 1. Create an empty list called my_list
my_list = []

# 2. Append the following elements: 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("After appending:", my_list)

# 3. Insert the value 15 at the second position (index 1)
my_list.insert(1, 15)
print("After inserting 15 at index 1:", my_list)

# 4. Extend my_list with another list [50, 60, 70]
new_list = [50, 60, 70]
my_list.extend(new_list)
print("After extending:", my_list)

# 5. Remove the last element
del my_list[-1]
print("After removing last element:", my_list)

# 6. Sort my_list in ascending order
my_list.sort()
print("After sorting:", my_list)

# 7. Find and print the index of the value 30
index_of_30 = my_list.index(30)
print("The index of 30 is:", index_of_30)