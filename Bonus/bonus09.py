password = input("Enter a new password: ")

result = {}

if len(password) >= 8:
    result["Length "] = True
else:
    result["Length "] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True

result["Digits "] = digit

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True

result["Uppercase "] = uppercase

if all(result.values()):
    print("Strong Password ")
else:
    print("Weak Password ")