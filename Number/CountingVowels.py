# Count the number of vowels in a given string.

str= "Adarsh"

l=['a','e','i','o','u']
ans=[]

intmed=str.lower()
print(f"String after converting to lower: {intmed}")

for i in str:
    if i in l:
        ans.append(i)
    else:
        continue

result=len(ans)

print(f"The count of number of vowels in a given string is : {result}")



# python CountingVowels.py