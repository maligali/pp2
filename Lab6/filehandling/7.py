first = open("sample.txt", "r")
second = open("file.txt", "a")
second.write(first.read())