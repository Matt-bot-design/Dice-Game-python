# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 01:33:59 2020

@author: Matthew Davids
"""
## So this is a DICE GAME there are two dice and two players, when rolling the dice prints
## out random numbers.
## The one who throughs the higest number gets 1 point and wins that round,
## when you run it again and the same person wins again his points increase by 1 until you end
## the game, when you do not want to roll again, it will out who won 

import random # imported random module to get random numbers
import time   # adding time module 

def gen_rand(): # defining generate random function
    rolldice = random.randint(1, 6) # assigning variable rolldice to the random numbers between 1 and 6
    return rolldice                 # returning the variable rolldice

def user_func(): # defining user function NOTE going to need to call this function in order to run code
    
    name1 = input("Enter Player 1 Name: ") 
    #name1 has the input() where user will input his name it is stored within name1 the value
    name2 = input("Enter Player 2 Name: ") 
    #name2 has the input() where user will input his name it is stored within name2 the value
    user1 = 0  # variable to hold dice value
    user1_wins = 0
    user2 = 0  # variable to hold dice value
    user2_wins = 0
    roll_again = "yes" 
    
    while roll_again == "yes": # while roll_again has the string 'yes' bottom code will continously run
            print("May luck be with you begin the roll....")
            time.sleep (random.randint (1,3)) #wait between 1 to 3 seconds before random numbers will generate
            user1 = gen_rand() # Assigning user1 variable to gen_rand() function which holds and returns random numbers
            user2 = gen_rand() # Assigning user2 variable to gen_rand() function which holds and returns random numbers
            print(f"{name1} rolls: {user1}") # using string concatenation with format(),f places variable in {} and prints out the value with in them
            print(f"{name2} rolls: {user2}") # The same as the top 
        
        # So the if-elif-else statement will print out who of the players got the highest number or if they equalled each other
            if user1 == user2: 
                print("It is a Draw") #It will be a draw if they equal each other
            elif user1 > user2: # else if statement- if player1 value higher than player2 value, player1 wins 
                print(f"{name1} wins")
                user1_wins += 1 # Adding 1 to user1 wins when getting a higher number
            else:
                print(f"{name2} wins") # And last if user1 not equal or bigger user2 then user two win
                user2_wins += 1 # Adding 1 to user2 wins when getting a higher number
                    
            
            roll_again = input("Want to play again: ") # if this variable recieves and input other than "yes" it will break out of the while loop and continue
            roll_again = roll_again.lower() # making all input or string value in roll_again lowercase
    # Lastly when roll_again recieves any other string that is not "yes" it will break out of while loop
    # And will come to this if statement when game is done the winner will be shown and the amount of points
    
    if user1_wins == user2_wins: # if the users win equal one another it is a draw
        print('It is a draw')
    elif user1_wins > user2_wins: #unless user1 wins is higher than user2 wins then user1 wins
        print(f'{name1} wins with {user1_wins} points') # using f format() to print out name1 value and user1_wins value
    else:
        print(f'{name2} wins with {user2_wins} points')
        