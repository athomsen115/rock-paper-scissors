#!/usr/bin/env python

#Rock, Paper, Scissors Game
import random
import string


# "Scissors cuts paper, paper covers rock, rock crushes lizard, 
# lizard poisons Spock, Spock smashes scissors, scissors decapitates lizard, 
# lizard eats paper, paper disproves Spock, Spock vaporizes rock, 
# and as it always has, rock crushes scissors."

#Game initialization
while 1:
    answer = raw_input('Hello!! Would you like to play a game? ').lower()
    
#Answer sanitization    
    if not answer.isalpha():
        print('you have entered an incorrect answer. please enter yes or no! \n')
        continue;
    if answer == 'yes' or answer == 'y':
        print('We will be playing rock, paper, scissors, lizard, spock.')
        count = 0
        playerCount = 0
        computerCount = 0
        # Input from player
        while count < 3:
            response = raw_input('Please enter Rock, Paper, Scissors, Lizard, or Spock (type quit to end): ').lower()
            #print 'You have entered: {}'.format(response) #For testing purposes
        
# Need random number (1-3) associated with Rock, Paper and Scissors
            randomInt = random.randint(1, 5)

            if randomInt == 1:
                randomVal = "rock"
            elif randomInt == 2:
                randomVal = "paper"
            elif randomInt == 3:
                randomVal = "scissors"
            elif randomInt == 4:
                randomVal == "lizard"
            elif randomInt == 5:
                randomVal == "spock"
            #print '{}, {}'.format(randomInt, randomVal) #For testing purposes
                
# Compare the strings
            if response == randomVal:
                print ('Tie! Choose again!')
            elif response == 'rock':
                if randomVal == 'paper':
                    print('Bummer! {} covers {}'.format(randomVal, response))
                    count += 1
                    computerCount += 1
                elif randomVal == 'scissors':
                    print('Winner! {} smashes {}'.format(response, randomVal))
                    count += 1
                    playerCount += 1
                elif  randomVal == 'lizard':
                    print('Winner! {} crushes {}'.format(response, randomVal))
                    count += 1
                    playerCount += 1
                elif randomVal == 'spock':
                    print('Bummer! {} vaporizes {}'.format(randomVal, response))
                    count += 1
                    computerCount += 1
            elif response == 'scissors':
                if randomVal == 'rock':
                    print('Bummer! {} smashes {}'.format(randomVal, response))
                    count += 1
                    computerCount += 1
                elif randomVal == 'paper':
                    print('Winner! {} cuts {}'. format(response, randomVal))
                    count += 1
                    playerCount += 1
                elif  randomVal == 'lizard':
                    print('Winner! {} decapitates {}'.format(response, randomVal))
                    count += 1
                    playerCount += 1
                elif randomVal == 'spock':
                    print('Bummer! {} smashes {}'.format(randomVal, response))
                    count += 1
                    computerCount += 1
            elif response == 'paper':
                if randomVal == 'scissors':
                    print('Bummer! {} cut {}'.format(randomVal, response))
                    count += 1
                    computerCount += 1
                elif randomVal == 'rock':
                    print('Winner! {} covers {}'. format(response, randomVal))
                    count += 1
                    playerCount += 1
                elif  randomVal == 'lizard':
                    print('Bummer! {} eats {}'.format(randomVal, response))
                    count += 1
                    computerCount += 1
                elif randomVal == 'spock':
                    print('Winner! {} disproves {}'.format(response, randomVal))
                    count += 1
                    playerCount += 1
            elif response == 'lizard':
                if randomVal == 'scissors':
                    print('Bummer! {} decapitates {}'.format(randomVal, response))
                    count += 1
                    computerCount += 1
                if randomVal == 'rock':
                    print('Bummer! {} crushes {}'.format(randomVal, response))
                    count += 1
                    computerCount += 1
                elif randomVal == 'paper':
                    print('Winner! {} eats {}'. format(response, randomVal))
                    count += 1
                    playerCount += 1
                elif randomVal == 'spock':
                    print('Winner! {} poisons {}'.format(response, randomVal))
                    count += 1
                    playerCount += 1
            elif response == 'spock':
                if randomVal == 'rock':
                    print('Winner! {} vaporizes {}'. format(response, randomVal))
                    count += 1
                    playerCount += 1
                elif randomVal == 'paper':
                    print('Bummer! {} disproves {}'.format(randomVal, response))
                    count += 1
                    computerCount += 1
                elif randomVal == 'scissors':
                    print('Winner! {} smashes {}'.format(response, randomVal))
                    count += 1
                    playerCount += 1
                elif  randomVal == 'lizard':
                    print('Bummer! {} poisons {}'.format(randomVal, response))
                    count += 1
                    computerCount += 1
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
