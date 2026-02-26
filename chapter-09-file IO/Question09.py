with open("log.txt", "r") as file:
    content = file.read()

with open("log2.txt", "r") as f:
    content2 = f.read()

    if content == content2:
        print("\n The content of both files is identical & matches the content of another file. .")
    else:
        print("\n The content of both files is different.")