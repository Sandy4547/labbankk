correct_username = "Sarayut"
correct_password = "1234"

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == correct_username:
    if password == correct_password:
        print("login success!")
    else:
        print("your password incorrect!")
else:
    print("your user incorrect!")