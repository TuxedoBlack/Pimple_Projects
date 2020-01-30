#correct way to develop dice roll
import random

min = 1 
max = 6
n = 'Thanks for Rolling!'

print ('Welcome to Dice Roll! What is your name')
name = input()
print (f'Welcome {name}! say roll to find out your 5 dice roll!')

roll_again = input()


while roll_again == 'roll' or roll_again == 'R' or roll_again == 'Roll' :
    print ('Rolling the dice...')
    print ('Your roll is...')
    print (random.randint(min,max))
    print (random.randint(min,max))
    print (random.randint(min,max))
    print (random.randint(min,max))
    print (random.randint(min,max))
    roll_again = (input('Roll the dice again?'))

while roll_again == 'no' or roll_again == 'n':
    print (n)
    break
#cant add else...but another while loop works! add 4 more dice to the roll_again
