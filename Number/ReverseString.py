# Reverse a string without using built-in functions.
str=input("Give the string : ")

s=0
e=len(str)-1

intmed=[]
while s<=e:
    intmed.append(str[e])
    e-=1

ans="".join(intmed)

print(f"The reversed string is : {ans}")








# python ReverseString.py