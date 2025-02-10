import random

def hangman():
    words = ["python", "java", "ruby", "swift"]
    word = random.choice(words)
    guessed = "_" * len(word)
    attempts = 6
    
    print("Welcome to Hangman!")
    
    while attempts > 0 and "_" in guessed:
        print(guessed)
        guess = input("Guess a letter: ")
        
        if guess in word:
            new_guessed = ""
            for i in range(len(word)):
                if word[i] == guess:
                    new_guessed += guess
                else:
                    new_guessed += guessed[i]
            guessed = new_guessed
        else:
            attempts -= 1
            print(f"Wrong guess! {attempts} attempts left.")
    
    if "_" not in guessed:
        print(f"Congratulations! You guessed the word: {word}")
    else:
        print(f"Game over! The word was: {word}")
        
hangman()
