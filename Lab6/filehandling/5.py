list = ["cocoa", "coffee", "tea"]
text = open("file.txt", "w")
text.write(", ".join(list))