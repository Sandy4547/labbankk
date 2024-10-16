def calculate_average():
    numbers = []
    while True:
        user_input = input("Enter number or exit('e', 'E', 'exit'): ")
        
        if user_input in ['e', 'E', 'exit']:
            break
        else:
            try:
                number = float(user_input)
                numbers.append(number)
            except ValueError:
                print("Invalid input, please enter a number or one of the exit commands ('e', 'E', 'exit').")
    
    if numbers:
        average = sum(numbers) / len(numbers)
        print("Average is {:.1f}".format(average))
    else:
        print("No numbers were entered.")

calculate_average()