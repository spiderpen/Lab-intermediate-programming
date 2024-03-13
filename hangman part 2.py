word = "spidey"
correct_letters = []
chances = 6 

while chances <= 6:
    guess = input("Guess the letters")   

    if len(guess) !=1:
        print("Give me only one letter")
    elif not guess.isalpha():
        print("Please give me one letter")
    elif guess.lower() in correct_letters:
        print("You already guessed the letter")
    else: 
        correct_letters.append(guess.lower()) 
        if guess.lower() in word.lower():
            print("Yay, you guessed it")
        else:
            chances -= 1
            print("Nice try, you have {} chances left.".format(chances))


    

    


