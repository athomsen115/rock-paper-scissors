#!/usr/bin/env python

#Rock, Paper, Scissors Game
import random
import string

#Game initialization
while 1:
    answer = raw_input('Hello!! Would you like to play a game? ').lower()
    
#Answer sanitization    
    if not answer.isalpha():
        print('you have entered an incorrect answer. please enter yes or no! \n')
        continue;
    if answer == 'yes' or answer == 'y':
        print('We will be playing rock, paper, scissors.')
        count = 0
        playerCount = 0
        computerCount = 0
        # Input from player
        while count < 3:
            response = raw_input('Please choose Rock, Paper or Scissors (type quit to end): ').lower()
            #print 'You have entered: {}'.format(response) #For testing purposes
        
# Need random number (1-3) associated with Rock, Paper and Scissors
            randomInt = random.randint(1, 3)

            if randomInt == 1:
                randomVal = "rock"
            elif randomInt == 2:
                randomVal = "paper"
            elif randomInt == 3:
                randomVal = "scissors"
            #print '{}, {}'.format(randomInt, randomVal) #For testing purposes
                
# Compare the strings
            if response == randomVal:
                print ('Tie! Choose again!')
            elif response == 'rock':
                if randomVal == 'paper':
                    print('Bummer! {} covers {}'.format(randomVal, response))
                    count += 1
                    computerCount += 1
                else:
                    print('Winner! {} smashes {}'. format(response, randomVal))
                    count += 1
                    playerCount += 1
            elif response == 'scissors':
                if randomVal == 'rock':
                    print('Bummer! {} smashes {}'.format(randomVal, response))
                    count += 1
                    computerCount += 1
                else:
                    print('Winner! {} cuts {}'. format(response, randomVal))
                    count += 1
                    playerCount += 1
            elif response == 'paper':
                if randomVal == 'scissors':
                    print('Bummer! {} cut {}'.format(randomVal, response))
                    count += 1
                    computerCount += 1
                else:
                    print('Winner! {} covers {}'. format(response, randomVal))
                    count += 1
                    playerCount += 1
            elif response == 'quit':
                break
            else:
                print('You have not entered a valid response. Please try again.')
        if playerCount > computerCount:
            print('Congratulations! You have beat the computer {} to {}\n'.format(playerCount, computerCount))
        elif computerCount > playerCount:
            print('Awww... you lose! The computer won {} to {}.\n'.format(computerCount, playerCount))
        else:
            print('There was no winner. Play again soon!\n')
                    
    elif answer == 'no' or answer == 'n':
        print('you have entered no\n')
        break
    else:
        print('you have entered an incorrect answer. please enter yes or no! \n')
        continue;
