from app1.Bonus.parsers14 import parse, convert

feet_inches = input("Enter feet and inches: ")

parsed = parse(feet_inches)
result = (convert(parsed["feet"], parsed["inches"]))

print(f"{parsed['feet']} feet and {parsed['inches']} is equal to {result}")

#print(f"{feet} feet and {inches} are equal to {meters}.")
if result < 1:
    print("Your kid is a midget and is too small.")
else:
    print("Your kid can use the slide.")