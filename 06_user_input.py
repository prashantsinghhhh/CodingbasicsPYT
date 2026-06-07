#input ()    =       Learning about accepting user input
#                    A function which promtes the user to enter the data
#                    then reurns the entered data as a string

# input("what is your name? ")- This is used to take input, assigning it to a variable will store the value

name= input("What is your name? ")
age = input("How old are you?")

print(f"cool your name is {name}")
print(f"you are {age} old")
#   LETS NOW INCREASE THE AGE BY 1

age = int(age) 

# Type casting the returned data from input to INT (as it was stored as STRING) 
# OR WE CAN DIRECTLY TAKE THE INPUT AS INT
# House_no = int(input("what is your House number"))

age += 1
print(f"your +1 age is {age}")

house_no = int(input("What is your house no ?")) # Taking input with data type

house_no += 1

print(f"your house number is {house_no}")
print(f"your house number +1 is {house_no}")
