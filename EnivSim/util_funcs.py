import math
import random

WIDTH = 1000
HEIGHT = 500

MUTATE_STEP = 20

def randomly_add_or_sub():
    return 1 if random.random() < 0.5 else -1

def distance(creature1, creature2):
    return(math.sqrt((creature1._xpos - creature2._xpos)**2 + (creature1._ypos - creature2._ypos)**2))
    
def _mutate(pcolor, mutate_rate):
    
    cred, cgreen, cblue = pcolor
    
    if(random.random() > 1 - mutate_rate):
        cred = pcolor[0] + randomly_add_or_sub() * MUTATE_STEP
        if(cred < 0):
            cred = 0
        elif(cred > 255):
            cred = 255
    if(random.random() > 1 - mutate_rate):
        cgreen = pcolor[1] + randomly_add_or_sub() * MUTATE_STEP
        if(cgreen < 0):
            cgreen = 0
        elif(cgreen > 255):
            cgreen = 255
    if(random.random() > 1 - mutate_rate):
        cblue = pcolor[2] + randomly_add_or_sub() * MUTATE_STEP
        if(cblue < 0):
            cblue = 0
        elif(cblue > 255):
            cblue = 255

    return((cred, cgreen, cblue))


def plant_spread_pos(creature, _pos, side):
    
    newpos = int(_pos + randomly_add_or_sub() * random.random() * creature.PLANT_SPREAD)
    #newpos = int(_pos + randomly_add_or_sub() * creature.PLANT_SPREAD)
    
    if(side == 'w'):
        newpos = newpos if(newpos < WIDTH) else int(random.random()*WIDTH)
    else:
        newpos = newpos if(newpos < HEIGHT) else 10+int(random.random()*(HEIGHT-10))
    newpos = newpos if(newpos > 0) else 0
    return(newpos)
