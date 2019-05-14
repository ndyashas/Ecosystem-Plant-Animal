'''
    This is a 2D World of creatures that live with some set of rules as given
    below
    
    1) 2 types of creatures:
        * Plants:
            - Have color
        * Animals:
            - Eat plants to gain energy
'''

import random
import creature as cr

WIDTH = 500
HEIGHT = 500

INITIAL_PLANT_POPULATION_SIZE = 50
plants = [cr.Plant((59, 189, 33), int(random.random()*WIDTH), int(random.random()*HEIGHT)) for i in range(INITIAL_PLANT_POPULATION_SIZE)]

def setup():
    background(255, 255, 255)
    size(WIDTH, HEIGHT)
    
    
def draw():
    fill(0)
    background(255, 255, 255)
    text("Plant count {}".format(len(plants)), 380, 10)
    
    for plant in plants:
        plant.render()
        plant.update_time_step(plants)
