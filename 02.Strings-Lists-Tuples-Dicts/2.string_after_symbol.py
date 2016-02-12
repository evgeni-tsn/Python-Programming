text = input("Enter text: ")
word = input("Enter word: ")

if word in text:
	print(text.split(word, 1)[1])
else:
	print("No such word found")