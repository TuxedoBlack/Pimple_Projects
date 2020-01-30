#correct way to develop dice roll
import random

min = 1
max = 6
roll_again = 'yes'
n = 'Thanks for Rolling!'

while roll_again == 'yes' or roll_again == 'y':
    print ('Rolling the dice...')
    print ('Your roll is...')
    print (random.randint(min,max))
    print (random.randint(min,max))
    print (random.randint(min,max))
    print (random.randint(min,max))
    print (random.randint(min,max))
    roll_again = (input('Roll the dice again?'))

while roll_again != 'yes' or roll_again == 'y':
    print (n)
    break
#cant add else...but another while loop works! add 4 more dice to the roll_again
    