import random


words = ["COMPUTER","TELESCOPE","SMARTPHONE",'UMBRELLA']
word = random.choice(words)

total_chances = 7
guesses_word = "_"*len(word)
while total_chances != 0:
    print(guesses_word)

    letter = input("Guess a letter: ").upper()
    if letter in word:
        for index in range(len(word)):
            if word[index] == letter:
                guesses_word = guesses_word[:index] + letter + guesses_word[index+1:]
                print(guesses_word)
        if guesses_word == word:
            print("You guessed the word!")
            break
    else:
        total_chances -= 1
        print("Incorrect Guess")
        print("Renaining chances are",total_chances)

else:
    print("Game Over")
    print("You Lost")
    print("All chances are exhausted")
    print("Correct word is",word)


