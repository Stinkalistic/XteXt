name = input("what do you want the file to be named?")
extension = input("what file type extension do you want?")
extension = "." + extension
name = name  + extension
text = input("write the text here: ")
with open(name,"w") as file:
	file.write(text)