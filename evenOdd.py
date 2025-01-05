import random

print("Welcome to the Even or Odd Game!")
print("You will be given a number. Guess if it's even or odd.\n")

# Game loop
while True:
    number = random.randint(1, 100)
    print(f"The number is: {number}")
    guess = input("Is it 'even' or 'odd'? ").lower()

    if (number % 2 == 0 and guess == "even") or (number % 2 != 0 and guess == "odd"):
        print("Correct! 🎉")
    else:
        print("Wrong! 😞")

    # Replay option
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break
