# Check if a number is positive, negative, or zero.

a=int(input("Give the number : "))

if a<0:
    print(f"{a} is a negative number")
elif a==0:
    print(f"{a} is equal to zero")
elif a>0:
    print(f"{a} is a positive number")