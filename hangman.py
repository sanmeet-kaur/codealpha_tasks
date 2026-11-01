import random

def hangman():
    words = ["python", "robot", "coding", "laptop", "program"]

    secret_word = random.choice(words)

    guessed_letters=[]
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("\n" + "=" *35)
    print("Welcome to Hangman")
    print("="*35)
    print("Guess the word, one letter at a time")
    print("You have 6 incorrect guesses available")
    print("_ " * len(secret_word))

    while incorrect_guesses<max_incorrect_guesses:
        print("\nWord: ", end="")

        for letter in secret_word:
            if letter in guessed_letters:
                print(letter, end="")
            else:
                print("_",end="")

        print()
        print("Guessed letters:", ", ".join(guessed_letters) if guessed_letters else "None")
        print(f"incorrect guesses remaining: {max_incorrect_guesses-incorrect_guesses}")

        guess= input("Enter a letter : " ).lower().strip()

        if len(guess)!=1 or not guess.isalpha():
            print("Invalid input! Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed this letter. Try another one.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Correct guess!")

            if all(letter in guessed_letters for letter in secret_word):
                print("Congratulations! You guessed the word", secret_word)
                break

        else:
            incorrect_guesses+=1
            print("Wrong guess!")

    else:
        print("Game over!")
        print("The correct word was: ", secret_word)

def main():
    while True:
        hangman()

        play_again= input("Would you like to play again? (yes/no): ").lower().strip()

        if play_again not in ("yes", "y"):
            print("\nThankyou for playing.")
            break

if __name__ == "__main__":
    main()


