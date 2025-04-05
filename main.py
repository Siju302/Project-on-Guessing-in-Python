import random
n = random.randrange(1,10)
guess = int(input("Enter any number: "))
while n!= guess:
    if guess < n:
        print("Number is too low")
        guess = int(input("Enter number again: "))
    elif guess > n:
        print("Number is too high")
        guess = int(input("Enter number again: "))
    else:
        break
print("You guessed correct!")