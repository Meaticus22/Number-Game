import random
answer = random.randint(1,10)

print("Guess the number from 1 to 10!")
guess = int(input("Your guess: "))

if guess == answer:
  print("Correct!")
else:
  print("Wrong, what is wrong with you! The answer was",answer)
