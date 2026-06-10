# compound intereset- intreset which adds compundly
# formula A = P *(1+r/100)^t 
# A = FINAL AMOUNT
# P = PRINCIPAL AMOUNT
# r = INTEREST RATE
# t = TIME
# n  = How many times does componding happen in a specific time period#

principle = 0
rate      = 0
time  = 0

while principle <= 0:
   principle= int(input("Enter the amount: "))
   if principle <=0:
      print("0 and -ve not allowed")

while rate <= 0:
   rate = int(input("Enter the rate: "))
   if rate <=0:
      print("0 and -ve not allowed")

while time <= 0:
   time= int(input("Enter the time: "))
   if time <=0:
      print("0 and -ve not allowed")

print(principle)
print(rate)
print(time)
a= principle*pow((1+rate/100),time)

print(f"Your Final amount is {a}")