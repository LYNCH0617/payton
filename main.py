# Step 1: Create a list of five favorite fruits and print it
fruits = ["Apple", "Banana", "Mango", "Orange", "Pineapple"]
print("Original list of fruits:", fruits)

# Step 2: Add two more fruits to the list and print the updated list
fruits.append("Strawberry")
fruits.append("Grapes")
print("Updated list of fruits:", fruits)

# Step 3: Remove the first fruit from the list and print the result
fruits.pop(0)
print("List after removing the first fruit:", fruits)

# Step 4: Sort the list in alphabetical order and print it
fruits.sort()
print("Sorted list of fruits:", fruits)

# Step 5: Print the length of the list
print("Length of the list:", len(fruits))


# Step 1: Create a tuple of four cities you want to visit
cities = ("Paris", "New York", "Tokyo", "Sydney")
print("Original tuple of cities:", cities)

# Step 2: Attempt to add another city to the tuple (this will raise an error)
try:
    cities.append("London")
except AttributeError as e:
    print(f"Error: {e} - You cannot add a city to a tuple because tuples are immutable.")

# Explanation: Tuples are immutable, meaning their elements cannot be changed once created.
# This is why the `append` method does not exist for tuples, resulting in an AttributeError.

# Step 3: Access and print the second city in the tuple
second_city = cities[1]
print("The second city in the tuple is:", second_city)

# Step 4: Check if a city is in the tuple (e.g., “Tokyo”) and print the result
is_tokyo_in_tuple = "Tokyo" in cities
print("Is Tokyo in the tuple?", is_tokyo_in_tuple)

full_name = "Maraiah Queen Arceta"
print("Full name:", full_name)

uppercase_name = full_name.upper()
print("Uppercase:", uppercase_name)

name_list = full_name.split()
print("Split in to list of words:", name_list)

hyphenated_name = "-".join(name_list)
print("Hyphenated name:", hyphenated_name)

reversed_name = " ".join(reversed(name_list))
print("Reversed name:", reversed_name)

name_length = len(full_name)
print("Length of the full name (including spaces):", name_length)

