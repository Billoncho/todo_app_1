#
# Coding Exercise 1
# Create a program that:
#
# 1. Prompts the user to input a (dollar) amount.
#
# 2. Calculates the corresponding amount in euros, given an exchange rate of 2.
#
# 3. Prints out the amount in euros.

rate = 2

dollar = float(input("Enter a dollar amount: "))
euros = (rate * dollar)
print(euros)