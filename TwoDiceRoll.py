import random
min = 1
max = 6

def rollDice():
    x  = random.randint(min, max)
    y = random.randint(min, max)
    return(x, y)

#Test
#print(rollDice())