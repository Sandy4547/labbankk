def introduce (sname, sage, scolor):
    print(f"Hello, my name is {sname}.")
    print(f"I am {sage} years old.")
    print(f"My favorite color is {scolor}")

def cel_to_fah(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
    
def average(x, y, z):
    return (x + y + z) / 2 - 1


def grade(score):
    if score >= 80:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"