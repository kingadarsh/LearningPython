# Find the largest of three numbers.

n1=int(input("The number 1 is : "))
n2=int(input("The number 2 is : "))
n3=int(input("The number 3 is : "))

# if n1>n2 and n1>n3:
#     print(f"{n1} is the largest")
# elif n1>n2 and n1<n3:
#     print(f"{n3} is the largest")
# elif n2>n1 and n2>n3:
#     print(f"{n2} is the largest")



# ########### ( OR ) ######### #

largest=max(n1,n2,n3)
print(f"{largest} is the largest number")


# python LargestOfThree.py