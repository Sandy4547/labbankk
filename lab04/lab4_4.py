def cel_to_fah(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
    
c = float(input("Type in a temperature in Celsius: "))
f = cel_to_fah(c)
print(f"That is {f} degrees Fahrenheit.")
37