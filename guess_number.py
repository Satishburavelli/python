import random
number=random.randint(1,100)

guess_num=0
while True:

    input_num=int(input("Enter a number:"))
    guess_num+=1
    if input_num==number:
        print("Guess is correct")
        break
    if input_num>number:
        print("Guess is too high")
    if input_num<number:
        print("Guess is too low")

