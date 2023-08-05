# Creating list
print("----------New List--------")
fruits = ['apple', 'banana', 'orange']
print(fruits)                       # Output: ['apple', 'banana', 'orange']

print("----------add element--------")
# Adding Element to List
fruits.append('grape')              # Add a single element
# Output: ['apple', 'banana', 'orange', 'grape']
print(fruits)

print("----------add elements--------")
fruits.extend(['watermelon', 'kiwi'])  # Add multiple elements
# Output: ['apple', 'banana', 'orange', 'grape', 'watermelon', 'kiwi']
print(fruits)


# Removing Element from List
print("----------remove element--------")
fruits.remove('banana')     # Remove 'banana'
# Output: ['apple', 'orange', 'grape', 'watermelon', 'kiwi']
print(fruits)

print("----------remove element from last--------")
popped_fruit = fruits.pop()  # Remove the last element and return it
print(popped_fruit)         # Output: kiwi
# Output: ['apple', 'orange', 'grape', 'watermelon']
print(fruits)


# Sort in new List
print("----------sort list(ASC) in new List--------")
sorted_fruits = sorted(fruits)
print(sorted_fruits)  # Output: ['apple', 'grape', 'orange', 'watermelon']

# Sorting in descending order
print("----------sort list(DESC) in new List--------")
sorted_fruits_desc = sorted(fruits, reverse=True)
print(sorted_fruits_desc)  # Output: ['watermelon', 'orange', 'grape', 'apple']

# The original list remains unchanged
print("----------Original list--------")
print(fruits)  # Output: ['apple', 'orange', 'grape', 'watermelon']


# Sorting List
# Sort inPlace
print("----------sort list(ASC) in place--------")
fruits.sort()  # Ascending Order (Default)
print(fruits)  # Output: ['apple', 'grape', 'orange', 'watermelon']

print("----------sort list(ASC) in place--------")
fruits.sort(reverse=True)  # Descending Order
print(fruits)  # Output: ['watermelon', 'orange', 'grape', 'apple']
