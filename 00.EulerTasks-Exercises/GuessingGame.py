import random

guess_this_number = (random.randint(1,100))
counter = 1

while(True):
    if counter is 1:
        enter_number = int(input("Enter number between 1 and 100: "))
    else:
        enter_number = int(input())

    if enter_number > 100 or enter_number < 1:
        print("Do not cheat! Enter number between 1 and 100")
        continue
    if enter_number is guess_this_number:
        print("Congrats! You got it in {} guesses".format(counter))
        break
    else:
        counter+=1
        if enter_number > guess_this_number:
            print("Too high. Try again: ", end='')
        else:
            print("Too low. Try again: ", end='')
