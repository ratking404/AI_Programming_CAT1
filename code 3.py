# Question 3: Lists and Loops

# Step 1: Create a list of student names
students = ["Monicah", "Irwine", "Benedict", "Gloria", "Faith", "Teddy", "Sandra", "Drina", "Ryan"]

# Step 2: Use a for loop to print each name in uppercase with its index number
for index, name in enumerate(students):
    print(f"{index + 1}. {name.upper()}")

