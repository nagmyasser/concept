import random

def word_scramble_game():
words_list = ['apple', 'banana', 'grape', 'orange', 'melon', 'cherry', 'mango', 'kiwi']
    
    
original_word = random.choice(words_list)
    
scrambled_word = list(original_word)
random.shuffle(scrambled_word)
scrambled_word = ''.join(scrambled_word)  
    
    
attempts = 5
    
print("Welcome to the Word Scramble Game!")
print(f"Try to guess the original word from the scrambled word: {scrambled_word}")
print(f"You have {attempts} attempts.")
    
while attempts > 0:
        
        guess = input("Your guess: ").strip().lower()
        
        
        if not guess:
            print("Please enter a valid word.")
            continue
        
        if guess == original_word:
            print("Congratulations! You guessed the word correctly!")
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Incorrect guess! You have {attempts} attempts left.")
            else:
                print(f"Sorry, you've run out of attempts. The original word was: {original_word}")


ord _scramble_game() # type: ignore

