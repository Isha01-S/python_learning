'''2. Write a python program using function to convert celcius to Fahrenheit.
°F = (9/5 × °C) + 32
'''

def fahrenheit(Celcius):
    return (((9/5)*Celcius) + 32)

a = fahrenheit(int(input("Enter the temperature in celcius : ")))
c=round(a,2)
print(c)