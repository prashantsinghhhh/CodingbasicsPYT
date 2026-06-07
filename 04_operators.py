
#Arithmatic Operators- (+,-,/,* etc)

a = 34
b = 5

c  = a+b 
#print(c)


#Assignemt Operators (=, += ,-= ,*= etc)
d = 4-2 # Assign 4-2 value to d
e = 3 # Assign 3 value to e
#print(e)

e += 2 # Increments the value of e by 2 and assigns it to e (e = e + 2)
#print(e)

e -= 2 # Decrements the value of e by 2 and assigns it to e (e = e - 2)
#print(e)

e *= 2 # Multiplies the value of e by 2 and assigns it to e (e = e * 2)
#print(e)

e /= 2 # Divides the value of e by 2 and assigns it to e (e = e / 2){ / give the quotient value}
#print(e)


#Comparision Operator (==, !=, >, <, >=, <=)
# NOTE- These operators return boolean values (True or False (1 or 0))

# Lets take new value F-
print()
f = 5<4 # IS 5 LESS THAN 4? FLASE
print("the value of f is: ",f)

f = 6>5 # IS 6 GREATER THAN 5? TRUE
print("the vlaue of f is", f)

f= 5 >=5 # IS 5 LESS THAN OR EQUAL TO 5? TRUE(IT IS EQAUL TO 5)
print("the vlaue of f is", f)

f = 5<=5  # IS 5 GREATER THAN OR EQUAK TO 5? TURE (EQUAL TO 5)
print("the vlaue of f is", f)

# Not EUAL TO- !=

f = 5!=4 # TRUE AS 5 IS NOT EQUAL TO 4
print("the vlaue of f is", f)

# EQUAL TO - ==

f = 5==5  # IS 5 EQUAL TO 5?? TRUE 
print("the vlaue of f is", f)

# NOTE: 
# "="  - THIS IS ASSIGNEMNT OPERATOR, ASSIGNS VALUES TO THE VARIABLE
# "==" - THIS IS COMPARISION OPERATOR, COMPARES THE VALUE WITH OTHER


#LOGICAL OPERATOR

# AND , OR , NOT , EXOR ,EXNOT
#OR TABLE

# OR - 1 OR 1 - 1(TRUE)
# OR - 1 OR 0 - 1(TRUE)
# OR - 0 OR 1 - 1(TRUE)
# OR - 0 OR 0 - 0(FALSE)

#AND TABLE

# AND - 1 AND 1 - 1 (TRUE)
# AND - 1 AND 0 - 0 (FALE)
# AND - 0 AND 1 - 0 (FALSE)
# AND - 0 AND 0 - 0 (FALSE)

#NOT TABLE- REVERS THE VALUE OF AND AND OR - TRUE TO FALSE, FALSE TO TRUE

#EX-OR (ONLY DIFFERNT VALUE TRUE AND REST FALSE)

# EX-OR - 1 EX-OR 1 - 0(FALSE)
# EX-OR - 1 EX-OR 0 - 1(TRUE)
# EX-OR - 0 EX-OR 1 - 1(TRUE)
# EX-OR - 0 EX-OR 0 - 0(TRUE)