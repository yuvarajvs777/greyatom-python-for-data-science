# --------------
# Code starts here

# Create the lists 

class_1 = ['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2 = ['Hilary Mason','Carla Gentry','Corinna Cortes']

# Concatenate both the strings
new_class = class_1 + class_2
print (new_class)

# Append the list
new_class.append('peter warden')

# Print updated list
print(new_class)

# Remove the element from the list
new_class.remove('Carla Gentry')


# Print the list
print(new_class)

# Create the Dictionary
course = {'Math':65,'English':70,'History':80,'French':70,'Science':60}

# Slice the dict and stores  the all subjects marks in variable

# Store the all the subject in one variable `Total`
Total = course['Math'] + course['English'] + course['History'] + course['French'] + course['Science'] 

# Print the total
print(Total)

# Insert percentage formula
percentage = Total/500*100

# Print the percentage
print(percentage)

# Create the Dictionary
mathematics = {'Geoffrey Hinton':78,'Andrew Ng':95,'Sebastian Raschka':65,'Yoshua Benjio':50,'Hilary Mason':70,'Corinna Cortes':66,'Peter Warden':75}

# Given string
max_marks_scored = max(mathematics,key = mathematics.get)
print (max_marks_scored)

# Create variable first_name 
first_name = max_marks_scored
print(first_name.split()[1])

# Create variable Last_name and store last two element in the list
Last_name = max_marks_scored
print(Last_name.split()[0])


# Concatenate the string


# print the full_name
Full_name = 'Ng Andrew'
print(Full_name)
# print the name in upper case
certificate_name = Full_name.upper()
print(certificate_name)
# Code ends here


