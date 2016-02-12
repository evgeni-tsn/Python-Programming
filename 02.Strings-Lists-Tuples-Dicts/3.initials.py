name = input("Enter name: ")
name_split = name.split()

initials = ""
for word in name_split:
	if word[0].isupper():
		initials += (word[0] + ". ")

print(initials.rstrip())