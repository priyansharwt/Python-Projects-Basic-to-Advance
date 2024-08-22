import random


n = random.randrange(1,10)
guess = int(input("Enter any number: "))
while n!= guess:
    if guess < n:
        print("Too low")
        guess = int(input("Enter number again: "))
    elif guess > n:
        print("Too high!")
        guess = int(input("Enter number again: "))
    else:
      break

print("\n꧁........✧･ﾟ: *✧･ﾟ:*Congratulations✧･ﾟ: *✧･ﾟ:*........꧂\n")
print("♡₊˚ 🦢・₊✧ YOU GUESSED IT RIGHT ૮꒰ ˶• ༝ •˶꒱ა ♡")
