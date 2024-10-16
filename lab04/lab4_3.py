def introduce (sname, sage, scolor):
    print(f"Hello, my name is {sname}.")
    print(f"I am {sage} years old.")
    print(f"My favorite color is {scolor}")
    
name = input("Enter your name: ")
age = input("Enter your age: ")
color = input("Enter your color: ")
introduce (name, age, color)