import random

wins = 0
losses = 0

def updateText(secret, error):
    global wins, losses
    
    guesses = []
    correct = False

    print("HUNGMANN AGAIN FELLAS!")

    while not correct:
        for letter in secret:
            if letter.lower() in guesses:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        print("")

        guess = input(f"Chances left {error}, Next Guess: ")
        guesses.append(guess.lower())
        if guess.lower() not in secret.lower():
            error -= 1
            if error == 0:
                break

        correct = True
        for letter in secret:
            if letter.lower() not in guesses:
                correct = False

    if correct:
        print(f"GOOD JOB! It was {secret}!")
        wins += 1
    else:
        print(f"WRONG! It was {secret}!")
        losses += 1

def play_game():
    global wins, losses

    secret_words = ["scorpion", "electro", "lizard", "venom", "kraven"]

    while secret_words:
        secret = random.choice(secret_words)
        secret_words.remove(secret)
        error = 6
        updateText(secret, error)
        print(f"Score: Wins - {wins}, Losses - {losses}")
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break

play_game()