from words import words
import random
import string

def select_valid_word(words):
    word=random.choice(words)
    while "_" in word or " " in word:
      word=random.choice(words)


    return word.upper()

#print(select_valid_word(words)) # this works fine until here
#now we are going to create a function wherein we will assign the value of word to the variable in the function


def hang():
    word=select_valid_word(words)
    word_letters=set(word)
    upper_case=set(string.ascii_uppercase)
    used_letters=set()


    lives=6

    while len(word_letters)>0 and lives >0:
        print(f"you have {lives} lives left ,play carefully and and you have used : ", "".join(used_letters))
        word_list=[letter if letter in used_letters else "_" for letter in word]
        print("current word :", "".join(word_list))

        user_input_letter=input("Enter a letter :").upper()
        if user_input_letter in upper_case-used_letters:
            used_letters.add(user_input_letter)
            if user_input_letter in word_letters:
                word_letters.remove(user_input_letter)
            else :
                lives-=1
                print('\n Your entered  letter,', user_input_letter ,'is not in word :')
        elif user_input_letter in used_letters:
            print('you have already used this letter, guess another letter :')
        else:
            print('that is not a valid letter')

    if lives==0:
       print('hangman died, the word was ', word)
    else:
       print('youve guessed the right word', word)


hang()