import string
from words import choose_word
from images import IMAGES




def get_hint(secret_word, letters_guessed):
    import random
    letters_not_guessed=[]
    index=0
    while(index < len(secret_word)):
        letter=secret_word[index]
        if letter not in letters_guessed:
            if letter not in letters_not_guessed:
                letters_not_guessed.append(letter)
        index+=1

    return random.choice(letters_not_guessed)


def is_word_guessed(secret_word, letters_guessed):
    if secret_word == get_guessed_word(secret_word, letters_guessed):
        return True
    return False

def get_guessed_word(secret_word, letters_guessed):
    index=0
    guessed_word=""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word+=secret_word[index]
        else:
            guessed_word+="_"
        index+=1

    return guessed_word


def  get_available_letters(letters_guessed):
    import string
    letters_left=string.ascii_lowercase

    for i in letters_guessed:
        letters_left = letters_left.replace(i,"")

    return  letters_left

def ifValid(user_input):
    if len(user_input)!=1:
        return False
    if not user_input.isalpha():
        return False
    return True


def hangman(secret_word):
   
    print ("Welcome to the game, Hangman!")
    print ("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print ("")

    print("aap abhi kitni difficulty pe yeh game khelna chahte hai:\n(a)  Easy \n(b)  Medium \n(c)  Hard \n")

    hint=0
    letters_guessed = []
    remaining_lives = 8
    user_difficulty_choice=input("Aapki choice a , b ya c ki terms me batayein:\n")
    total_lives=remaining_lives=8
    images=[0,1,2,3,4,5,6,7]
    if user_difficulty_choice not in ["a","b","c"]:
        print ("aapki choice invalid hai.\nGame easy mode main start kr rhe hai")
    else:
        if user_difficulty_choice=="a":
            total_lives=remaining_lives=8
            images=[0,1,2,3,4,5,6,7]
        elif user_difficulty_choice=="b":
            total_lives=remaining_lives=6
            images=[0,2,3,5,6,7]
        elif user_difficulty_choice=="c":
            total_lives=remaining_lives=4
            images=[1,3,5,7]

    while (remaining_lives>0):
        available_letters = get_available_letters(letters_guessed)
        print ("Available letters: " + available_letters)

        guess = input("Please guess a letter: ")
        letter = guess.lower()
        
        if (not ifValid(letter) and letter!="hint"):
            print ("invalid input")
            continue

        if hint==0:
            if letter == "hint":
                p=get_hint(secret_word, letters_guessed)
                print ("your hint for next character",p)
                hint+=1
                continue
        else:
            print ("you have all ready use hint !")
            print ("you can't use hint option !")
            print ("if you will use hint option, your one live will go !")


        if letter in secret_word:
            letters_guessed.append(letter)
            print ("Good guess: " + get_guessed_word(secret_word, letters_guessed))
            print ("")
            if is_word_guessed(secret_word, letters_guessed) == True:
                print (" * * Congratulations, you won! * * ")
                print ("")
                break

        else:
            print ("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
            print (IMAGES[images[total_lives-remaining_lives]])
            print ("remaining_lives: ",+(remaining_lives))
            print ("")
            letters_guessed.append(letter)
            remaining_lives-=1

    else:
        print ("sorry you lose the game, the word was - " + str(secret_word))
secret_word=choose_word()
hangman(secret_word)
