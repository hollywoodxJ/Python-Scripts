# Importing Files

from replit import clear
import random

from hangman_words import word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

from hangman_art import logo, stages
print(logo)


# Testing code
# print(f'Pssst, the solution is {chosen_word}.')
print(f"The word is '{word_length}' letters long.")


#Create blanks
guessedletters = []

display = []
for _ in range(word_length):
    display += "_"


# Guess the letter
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    clear()

    if guess in display:
      print(f"You've already guessed {guess}. Please choose another letter")
    guessedletters.append(guess)


#Check guessed letter if correct.
    for position in range(word_length):
        letter = chosen_word[position]
       
        if letter == guess:
            display[position] = letter
        
            
#Check if user is wrong.
    if guess not in chosen_word:
        print(f"You guessed the letter '{guess}'. That letter is not in the word. You lose a life!")
        lives -= 1
        
        if lives == 0:
            end_of_game = True


    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.

    print(stages[lives])
    print(f"You have guessed the letters {guessedletters}")
  
    print(f"You have {lives} lives remaining.")
    if lives == 0:
      print(f"The word was '{chosen_word}'.")
      print("YOU LOSE!")
    if "_" not in display:
        end_of_game = True
        print("YOU WIN.")