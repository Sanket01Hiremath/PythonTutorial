input_file = r'C:\Users\SanketHiremath\IdeaProjects\PythonTutorial\P3 D3 Assignment\input.txt'  # Replace 'example.txt' with the path to your text file
output_file = r'C:\Users\SanketHiremath\IdeaProjects\PythonTutorial\P3 D3 Assignment\output.txt'  # Replace 'example.txt' with the path to your text file

# Open the file in read mode
with open(input_file, 'r') as file:
    # Read the entire content of the file into a single string
    content = file.read()


# Open the file in read mode
with open(output_file, 'w') as file:
    # Read the entire content of the file into a single string
    file.write(content)
# Display the content of the file


