def convert(fl_oz):
    mil = float(fl_oz) * 29.57353
    return mil


result = fluid = input("Enter how many fluid ounces you would like to convert: ")

print(convert(result))