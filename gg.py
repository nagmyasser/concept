import random
def word_scramble_game():
    print ("Welcome to the word scramble game")
    print("unscramble the word to win the game.You have 5 attempts.\n")
    word_list = ["apple","banana","orange","mango", "juice"]
    original_word= random.choice(word_list)
    scrambled_word= "".join(random.sample(original_world,len(original_word)))
    attempts =5
    print(f"Here is your scrabled word:{scrambled_word}")
    while attempts>0:
        guess = input("Guess the original word: ").strip().lower()

        if not guess.isalpha():
            print("Invaled input. please enter letters only(no numbers or special characters ).\n")
            continue
        if guess == original_word:
            print("Congratulations you guesed thw word correctly!")
            return
        else:
            attempts-=1
            print(f"incorrect. You have {attempts}attempts left.\n")

    print(f"sorry you have ran out of attempts the correct word was{original_word}.Better luck next time")

word_scramble_game()             