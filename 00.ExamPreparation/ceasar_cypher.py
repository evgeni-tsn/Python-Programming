try:
    shift = input()
    text = input()
    def encrypt(message, shift):
        new = ''
        for i in (ord(x) for x in message):  # gets the ascii value of each letter in message
            if 64 < i < 91:  # uppercase letters
                new += chr(65 + (i + shift - 65) % 26)
            else:
                new += chr(i)
        return new

    print(encrypt(text, int(shift)))
except:
    print("INVALID INPUT")
