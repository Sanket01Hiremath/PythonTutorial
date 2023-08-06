# Integer variable
age = 25
print(age)
print(type(age))            # Output: <class 'int'>

# Float variable
temperature = 98.6
print(temperature)
print(type(temperature))    # Output: <class 'float'>

# String variable
name = "John Doe"
print(name)
print(type(name))           # Output: <class 'str'>

# List variable
fruits = ['apple', 'banana', 'orange']
print(fruits)
print(type(fruits))         # Output: <class 'list'>

# Tuple variable
coordinates = (10, 20)
print(coordinates)
print(type(coordinates))   # Output: <class 'tuple'>

# Dictionary example
person = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(person['name'])  # Output: Alice
print(person.get('age', 'default'))  # Output: 30
person = {'name': 'Alice', 'city': 'New York'}
print(person.get('age', 'default'))  # Output: default
print(type(person))        # Output: <class 'dict'>

#Set example
# Creating sets
fruits_set = {'apple', 'banana', 'orange'}
colors_set = set(['red', 'green', 'blue', 'red'])  # Duplicates are removed

print(fruits_set)   # Output: {'banana', 'apple', 'orange'}
print(colors_set)   # Output: {'red', 'green', 'blue'}

# Adding elements to a set
fruits_set.add('grape')
print(fruits_set)   # Output: {'banana', 'apple', 'grape', 'orange'}

# Removing elements from a set
fruits_set.remove('banana')
print(fruits_set)   # Output: {'apple', 'grape', 'orange'}

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union
print(set1.union(set2))   # Output: {1, 2, 3, 4, 5, 6}

# Intersection
print(set1.intersection(set2))   # Output: {3, 4}

# Difference
print(set1.difference(set2))     # Output: {1, 2}


#Boolean example
is_sunny = True
is_raining = False

print(is_sunny)    # Output: True
print(is_raining)  # Output: False

# Logical expressions
is_warm = True
is_summer = False

# AND operator
print(is_warm and is_summer)  # Output: False

# OR operator
print(is_warm or is_summer)   # Output: True

# NOT operator
print(not is_warm)            # Output: False










