contents = ["All carrots are to be sliced longitudinally.",
            "The carrots were reportedly sliced.",
            "The slicing process was well presented."]

filenames = ["doc.txt", "report.txt", "presentations.txt"]

for content, filename in zip(contents, filenames):  # Zip will put the contents side by side in a tuple. [("All", "Doc")]
    file = open(f"../files/{filename}", 'w')        # This will creat a file path to the variable in curly brackets.
                                                    # We need to go up one directory because the files folder in not in the bonus folder.
    file.write(content)                             # This will create the fils using the filenams list and write the contents list into each file.


# a = "I am a string " \       # If your string is very long, you can use the backslash so it will fit on the screen.
#     "on my " \               # Not working in Pycharm.
#     "own."       \

