import random
answer = random.randint(1,10)
print("Guess the number from 1 to 10!")
turn = 1

while True:
  turn += 1
  guess = int(input("Your guess: "))

  if guess == answer:
    turn -= 1
    print("")
    print("-----------------")
    print("Correct, Finally! It took you",turn,"tries!")
    print("-----------------")
    break
  elif answer > guess:
    print("The answer is higher pal!")
    print("|")
  else:
    print("The answer is lower too much!")
    print("|") 
