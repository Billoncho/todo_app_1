# Coding Exercise 3
# Extend the given code so the code prints out a list containing the same items as floats.
#
# The output of your code should be as below:
#
# [10.0, 19.1, 20.0]

user_entries = ['10', '19.1', '20']

user_floats = [round(float(i), 1) for i in user_entries]

print(user_floats)