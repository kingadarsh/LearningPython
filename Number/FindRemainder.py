# Find the remainder when a number is divided by another.



divisor=int(input("Give the Divisor : "))
dividend=int(input("Give the Quotient : "))

if divisor == 0:
    print("Divisor has to be greater than 0")
else:
    ans=dividend%divisor
    print(f"Remainder is : {ans}")






# python FindRemainder.py