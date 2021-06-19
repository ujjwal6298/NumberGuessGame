#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
attempts_list=[]


# In[2]:


def show_score():
    if len(attempts_list) <=0:
        print("There is currently no high score, it's yours for the taking!")
    else:
        print("The current high score is {} attempts".format(min(attempts_list)))
def start_game():
    random_number= int(random.randint(1,10))
    print("Hello Traveller! Welcome to the Game of Guesses! ")
    player_name= input("what's your name?\n")
    wanna_play= input("Hi, {}, would you like to play the guessing game? (Enter yes/no)".format(player_name))
    #where the show_score function used to be
    attempts=0
    show_score()
    while wanna_play.lower() =='yes':
        try:
            guess = input("pick a number between 1 and 10")
            if int(guess) <1 or int(guess)> 10:
                raise ValueError("Please guess a number within the given range")
            if int(guess) == random_number:
                print("Nice! uou got it!")
                attempts+=1
                attempts_list.append(attempts)
                print("It took you {} attempts".format(attempts))
                play_again= input("Would you like to give it a shot again? (Enter yes/no)")
                attempts=0
                show_score()
                random_number=int(random.randint(1,10))
                if play_again.lower() == "no":
                    print("That's cool, have a good one!")
                    break
            elif int(guess) > random_number:
                print("It's lower")
                attempts += 1
            elif int(guess) < random_number:
                print("It's higher")
                attempts += 1
        except ValueError as err:
            print("oh no!, that is not a valid value. Try again...")
    else:
        print("That's cool, have a good one!")
if __name__=='__main__':
    start_game()


# In[ ]:




