# note in python: int the range brack the start is inclusive and the end is exclusive- (start,end,incerment/decrement)

#printing number 1 to 5 in vertical
# 1
# 2
# 3
# 4
# 5 

# for x in range(1,6,1):
#     print(x)

# printing in horizontal - 1 2 3 4 5

# y=0
# for x in range(1,6,1):
#     y=y*10+x
# print(y)

# printing squre of a number from 1 to 5-

# for i in range (1,6,1):
#     print(i**2)

# # printing horizontally 

# for i in range (1,6,1):
#     print(i**2, end= " ")

# printing even number from 1 to 10

# for i in range(1,11,1):
#     if i % 2 ==0:
#         print(i, end=" ")

# sum of number 1 to 10 

# sum=0
# for i in range (1,11,1):
#     sum = sum+i
#     print(sum)


# reverse a word

# word = input("Give me the word to reverse: ")
# x = len(word)
# print(x)
# for i in range (0,x,1):
#     print(word[i], end=" ")
# print()
# # now lets reverse this- we will keep the range as X as strting and 0 as end and we will print it in -1 (so it will reduce it)
# print("in reverse order: ")
# for j in range (x-1,-1,-1):
#     print(word[j], end=" ")


# conunting vowels-
# vowel=["a","e","i","o","u","A","E","I","O","U"]
# count = 0
# word=input("Enter the Word to find vowles in it:  ")
# for i in range (0,len(word),1):
#     for j in range (0,len(vowel),1):
#         if word[i] == vowel[j]:
#             print(word[i])
#             count = count + 1
# print(count)

# we can use "in" here

# vowel= "aeiouAEIOU"
# word = input("input word: ")
# count = 0

# for i in range(0,len(word),1):
#     if word[i] in vowel:
#         print(word[i])
#         count = count+1
# print(count)


#fibonacci sequence- 0 1 1 2 3 5 8 13 21 34 

# first =  int(input("enter first num: "))
# second = int(input("enter vsecond num : "))
# next_num = 0
# print(first,end=" ")
# print(second,end=" ")
# for i in range (0,8,1):
#    next_num=first+second
#    first=second
#    second= next_num
#    print(next_num,end=" ")

#printin n fibonacci number where N is given by user

# n=int(input("How many number you need of fibonacci series: "))
# first= 0
# second= 1

# print(f"the {n} series is: ")
# if n <= 0:
#       print("invalid")
# elif n == 1:
#         print(first)
# elif n == 2:
#         print(first,second,end=" ")
# else:
#     print(first,second,end=" ")

#     for i in range(0,n-2,1):
#         next_num= first+second
#         first= second
#         second= next_num

#         print( next_num,end=" ")


# calculating factorial of a number
# 0 fact = 1
# 1 fact = 1x1 
# 2= 2x1
# 3= 3x2x1
# 4= 4x3x2x1#

# num= int(input("Enter the number to be factorial: "))
# pass

# if num<0:
#     print("Enter positive number")
# elif num==0:
#     print(1)
# else:
#     factorial= 1
#     for i in range(num,0,-1):
#         factorial= i*factorial
#     print(factorial)

# Number prime or not
# What is prime number?? it is only divisible by itself,1 #

# number= int(input("Enter the number to check prime or not: "))

# 5 > 4,3,2
# if number<=1:
#       print("Number should be more than 1 ")
# elif number == 2:
#     print("prime")
# else:
#     count = 0
#     for i in range(2,number,1):
#         if  number % i== 0:
#             count = 1
#     if count == 1:
#         print("not prime")
#     else:
#         print("prime")

# optimised wayy - use square root to check wheater num is prime or not
# used boolean for prime or not  and sqroot to find the , max range to divide: 
# if number<=1:
#       print("Number should be more than 1 ")
# elif number == 2:
#     print("prime")
# else:
#     is_prime= True
#     for  i in range ( 2,int(number**0.5)+1,1):
#         if number % i == 0:
#             is_prime= False
#             break
#     if is_prime:
#         print("prime")
#     else:
#         print(" not prime")

# print(int(number**0.5)+1)


# count number of time a letter has occured:

# bbrroo
word=input("Enter the word: ")
checked = ""
for i in range(0, len(word)):
    
    if word[i] in checked:
        continue
    count=0 
    for j in range(0, len(word)):
        if word[i]==word[j]:
            count += 1
    checked=checked+word[i] 
         
    print(count)
