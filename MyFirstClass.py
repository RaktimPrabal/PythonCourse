from random import randint
import sys

answer = randint(int(sys.argv[1]), int(sys.argv[2]))

while True:
    try:
        guess = int(input(f"guess a number {sys.argv[1]} ~ {sys.argv[2]}:  "))
        if int(sys.argv[1]) <= guess <= int(sys.argv[2]):
            if guess == answer:
                print("u are correct")
                break
        else:
            print("enter within the range")

    except ValueError:
        print("please provide a number")
