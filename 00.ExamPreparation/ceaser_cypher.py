shift = input()
text = input()
try:
    def encrypt(message, shift):
        new = ''
        for i in (ord(x) for x in message):  # gets the ascii value of each letter in message
            if 64 < i < 91:  # uppercase
                new += chr(65 + (i + shift - 65) % 26)
            elif 96 < i < 123:  # lowercase
                new += chr(97 + (i + shift - 97) % 26)
            else:
                new += chr(i)
        return new


    print(encrypt(text, int(shift)))
except:
    print("INVALID INPUT")
