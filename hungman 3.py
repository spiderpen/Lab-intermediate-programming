def updateText(secret, error):
  guesses = []
  correct = False

  while not correct:
      for letter in secret:
          if letter.lower() in guesses:
              print(letter, end=" ")
          else:
              print("_", end=" ")
      print("")

      guess = input(f"Chances Left {error}, Next Guess: ")
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
  else:
      print(f"WRONG! It was {secret}!")

# Calling the function with the initial values
updateText("spidermen", 6)