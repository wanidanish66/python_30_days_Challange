def l():
    words = [" apple ", "banana ", " mango", "banana"]
    words.remove("banana")
    for word in words:
        print(word.strip())
l()