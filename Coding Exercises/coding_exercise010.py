# Coding Exercise 2
# The ranking list given in the coding area represents the ranking of three athletes, John, Sen, and Lisa. John won 1st place, Sen got 2nd, and Lisa 3rd.
#
# Your task is to create a program that:
#
# 1. Contains the above list.
#
# 2. Prompts the user to input a rank number.
#
# 3. Returns the person who has the given rank.
#
#
#
# For example:

ranking = ['John', 'Sen', 'Lisa']

rank_num = int(input("Enter rank number: ")) -1
print(ranking[rank_num])
