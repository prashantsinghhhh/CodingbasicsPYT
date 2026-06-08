
#Format specifiers = {value: flags} flags can be 
# Format a value vased on flag speciifed
# :.(number)f - round of to that many number
# :(number) - allocate specified number of space
# :<       - left align
# :>        - right align
# :^         - center align
# :+         - use plus sign before the number to denote positive value
# :,          - commma sperator (ex- 2,000)
# :            - insert a space before number
# :=           - place sign to left most position

# lets try  # 

price1 = 312.23242
price2 = -123.222
price3 = 3312.2
print(f"Price 1 is {price1 :<+,.2f}")
print(f"Price 2 is {price2 :.2f}")
print(f"Price 3 is {price3 :.2f}")
#NOTE- DO NOT HAVE ANY SPACE AFTER .2f, JUST CLOSE THE BRACKET WITHOUT SPACE
# OR ELSE YOU'LL GET ERROR
