# Write Your Name into a File

with open("name.txt", "w") as file:
    file.write("Gowshick")
print("Name saved successfully!")

# Read the File

with open("name.txt", "r") as file:
    print(file.read())

 # Add Another Name

 with open("name.txt", "a") as file:
    file.write("\nKarthik")
print("Name added successfully!")

# Count Characters

with open("name.txt", "r") as file:
    data = file.read()
print("Characters:", len(data))

# Count Words

ith open("name.txt", "r") as file:
    data = file.read()
print("Words:", len(data.split()))

# Display Each Line

with open("name.txt", "r") as file:
    for line in file:
        print(line)


# Check a Name

name = input("Enter a name: ")

with open("name.txt", "r") as file:
    data = file.read()

if name in data:
    print("Name Found")
else:
    print("Name Not Found")