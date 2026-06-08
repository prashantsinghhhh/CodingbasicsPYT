
# VALIDATE USER INPUT 
# 1. USER NAME - NO MORE THAN 12
# 2. USER NAME - MUST NOT CONTAIN SPACES
# 3. USER NAME - MUST NOT CONTAIN DIGITS

# 1. len()                 -- to find length
# 2. string.isalpha()      -- to makesure no space and is only name
# 3. we can also find space -- string.find(" ")

print("WE ARE VALIDATING USERNAME")

username = input("Enter your username: ")

length = len(username)
if length <=12 and length > 0:
    if username.isalpha():
        print("username is validated")
    else:
        print("User name contain digits or space")
else:
    print("username must not be more than 12")

#BETTER CODE BELOW 

if len(username)> 12:
    print("Your username is more than 12")

elif not username.isalpha():
    print("Digits and space not allowed")
else:
    print(f"Welcome {username}")

# elif not username.find(" ") == -1:
#     print("No Space allowed")