# Indexing= Accessing element of a sequence using index operatior []
#                    [start : end : step]

# Start- which index/ from which range you want the elements from NOTE- It is inclusive
# end- range you want to end NOTE- it is exclusive
# Step - What patern you want to follow? step = 2 then every 2nd element is printed

credit_card = "1234-5678-9102"
print(credit_card.find("-"))

#finding 0th element in the sequence-

print(credit_card[1])   # ----1
print(credit_card[0:3]) # NOTE- It will print from 0th element to 2 not till three as end is exclusive
# ans - 123
print(credit_card[:3])# NOTE - if we want the starting digits and just want to stop at the end
                      #        then we can just specify the end and no need of start (:3)
print(credit_card[-1]) # NOTE - this will print the last digit
# ans - 0

#WRONG FORMAT:

#print(credit_card[-1:-3]) #NOTE - will print from -1 to -3 so only -1 and -2 elememnt- 0,1
# NOTE- the answer is not printed as we have fromatted is wrong, start will be -3 and end -1

print(credit_card[-3:-1])
# ans - 91
# NOTE- it gave us only till n-1 elemet as end is exclusive

#NOTE- to add all we can just simply ignore the end and keep it empty as by then we can print all number after the start

print(credit_card[-3:])
# ANS- 910

#NOTE - suppose we need to print only the last 4 digits of adhaar then??
# lets make a project for it

# print("Adhaar details")
# print(" ")
# adhaar= input("What is your adhaar number??: ")
# # 1234 1234 1234 - sample adhaar for finding index
# print(f"Your adhaar details have been secured safely xxxx xxxx {adhaar[-4:]}")

#USING STEPS
# credit_card = 1234-5678-9102
print(credit_card[::2]) #This will print every 2nd element from 1
#  13-6890
print(credit_card[::1]) # 3 This will print every next element from 1
# 1234-5678-9102
print(credit_card[::-1]) # This will print all the element in reverse order
# 2019-8765-4321


