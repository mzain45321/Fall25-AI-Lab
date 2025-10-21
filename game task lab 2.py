print("Welcome to Fizz Buzz Game ")

for number in range(1, 21): 
    if number % 3 == 0 and number % 5 == 0:
        correct_answer = "Fizz Buzz"
    elif number % 3 == 0:
        correct_answer = "Fizz"
    elif number % 5 == 0:
        correct_answer = "Buzz"
    else:
        correct_answer = str(number)


    user_answer = input(f"Your turn for {number}: ")


    if user_answer.strip().lower() == correct_answer.lower():
        print(" Correct!")
    else:
        print(f" Wrong! The correct answer was: {correct_answer}")
        break
else:
    print(" You completed the Fizz Buzz game ")

