# Coding Exercise 3
# We have defined the same ranking list as in the previous exercise:
#
#
#
# This time you should create a program that:
#
# 1. Contains the above list.
#
# 2 Prompts the user to input the person's name.
#
# 3. Returns the rank that person has.
#
#
#
# For example:

ranking = ['John', 'Sen', 'Lisa']

rank_name = input("Enter a name: ")
print(ranking.index(rank_name) + 1)

