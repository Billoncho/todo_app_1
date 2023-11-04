filenames = ["1.Raw data.txt", "2.Reports.tex", "3.Presentations.txt"]

for filename in filenames:
    filename = filename.replace('.', '-', 1)
    print(filename)