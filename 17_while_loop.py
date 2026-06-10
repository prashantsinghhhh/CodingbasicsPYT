
#WHILE LOOP

# let the loop run untill the user enter the name

# name= input("enter your name: ")

# while not name.find(" ") == -1 or name == "":       # if no named entered, it will continue to loop
#     print("space not allowed")
#     name= input("enter your name: ") # condition to go out from the loop

# print(f"HELLO {name}")


#correct age

# age = int(input("What is your age: "))

# while age<0 :
#     print("can't be negative")
#     age = int(input("What is your age: "))  # condition to break the loop
# print(age)


# input number b/ 1 and 10

num= int(input("enter the number b/w 1 -10 "))
while num<1 or num>10:
    print("number must be b/w 1-10")
    num= int(input("enter the number b/w 1 -10 "))

print(f"Your number is {num}")