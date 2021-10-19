# Asking Questions
# Using input function to insert values to variable and call it using functions
"""
print("How old are you?", end =' ')
age = input()
print("How tall are you?", end = ' ')
height = input()
print("How much do you weight?", end = ' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

"""
# Some additional questions

print("Do you realy like to learn python?  \n(if you agree type positive or negitive if you disagree)", end = ' ')
question_1 = input()
print("Which book now you are following?", end = ' ')
question_2 = input()

print(f"We are glad to hear your {question_1} opinion and we wish that you would learn the book named {question_2} that you are following.")

# Another type of input (Raw_input)
# Notes:  This function works in older version (like Python 2.x). Wont work on the letest versions of python
username = raw_input("Enter Username:")
# print("Username is : " + username)
