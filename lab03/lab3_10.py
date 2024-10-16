def determine_grade():
    score = float(input("Enter your score: "))
    
    if score > 79:
        grade = 'A'
    elif score > 69:
        grade = 'B'
    elif score > 59:
        grade = 'C'
    elif score > 49:
        grade = 'D'
    else:
        grade = 'F'
    
    print("Your grade is {}.".format(grade))

determine_grade()