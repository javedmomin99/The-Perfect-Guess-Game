import random
print("Welcome to the Perfect Guess Game")
print("You have to guess a number between 1 and 100")
random_choice = random.randint(1,100)
print(random_choice)
def javed():
  user_choice = int(input("What is your Guess?\n"))
  if user_choice == random_choice:
    print(f"You guessed it right. The number was {random_choice}")
  elif user_choice > random_choice:
    print("You guessed the wrong number.Pls enter a smaller number")
    javed()
  else:
    print("You guessed the wrong number.Pls enter a larger number")
    javed()
javed()
