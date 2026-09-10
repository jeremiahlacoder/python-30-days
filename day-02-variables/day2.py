# Day 2: 30 Days of python programming
 
firstName = "Jeremiah"
lastName = "Spencer"
fullName = firstName + ' ' + lastName
country = "USA"
city = "Memphis"
age = 20
curYear = 2026
is_married = False
is_true = True
is_light_on = False
parentName, school, lastYear = "Bathsheba Warren" , "Jackson State University", curYear - 1
 
print(type(fullName)) #used to get the type of variable
print(len(firstName)) #used to get the length of the variable
print(len(lastName))

num_one = 5
num_two = 4
value = num_one + num_two
print(value)
diff = num_two - num_one
print(diff)
division = num_one / num_two
product = num_two * num_one
remainder = num_two // num_one
print(product, division, remainder)

radius = input("What is the radius: ")
area_of_circle = 3.14* pow(int(radius), 2) #in order to bypass the error i used the "pow" keyword and converted the input into a int
circ_of_circle = 2*3.14*int(radius)
print(area_of_circle, circ_of_circle)

# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
userFirstName, userLastName, userCountry, userAge = input("What is your first name, last name, Country you reside in, and age: ").split() #used the keyword split to take multiple inputs for the different variables
print(userFirstName, userLastName, userCountry, userAge)



