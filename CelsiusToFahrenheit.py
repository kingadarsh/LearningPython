# Convert CelsiusToFahrenheit.


degr=float(input("Give the temprature : "))
scale=input("Give the current scale of the temprature (C/F): ")
if scale == "C":
    ans=(9/5)*degr+32
    print(f"The conversion of Celsius to Fahrenheit :{ans} ")
elif scale == "F":
    ans=(5/9)*(degr-32)
    print(f"The conversion of Fahrenheit to Celsius : {ans}")


# python CelsiusToFahrenheit.py