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
import util_funcs as uf

WIDTH = uf.WIDTH
HEIGHT = uf.HEIGHT

INITIAL_PLANT_POPULATION_SIZE = 25
INITIAL_ANIMAL_POPULATION_SIZE = 20

MAX_PLANT_POPULATION_SIZE = 500
MAX_ANIMAL_POPULATION_SIZE = 500

plants = [cr.Plant(int(random.random()*WIDTH), 10+int(random.random()*HEIGHT-10), (59, 189, 33)) for i in range(INITIAL_PLANT_POPULATION_SIZE)]
animals = [cr.Animal(int(random.random()*WIDTH),
                     10+int(random.random()*HEIGHT-10),
                     (int(random.random() * 255), int(random.random() * 255), int(random.random() * 255))) for i in range(INITIAL_ANIMAL_POPULATION_SIZE)]

def setup():
    background(255, 255, 255)
    size(WIDTH, HEIGHT)
    
    
def draw():
    fill(0)
    background(255, 255, 255)
    text("Plant count {} |".format(len(plants)), WIDTH - 100, 10)
    text("| Animal count {} |".format(len(animals)), WIDTH - 250, 10)
    
    for plant in plants:
        plant.render()
        plant.update_time_step(plants)
        
    for animal in animals:
        animal.render()
        animal.update_time_step(animals, plants)
        
    if(len(plants) > MAX_PLANT_POPULATION_SIZE):
        while(len(plants) > MAX_PLANT_POPULATION_SIZE):
            plants.remove(plants[-1])
        
    if(len(animals) > MAX_ANIMAL_POPULATION_SIZE):
        while(len(animals) > MAX_ANIMAL_POPULATION_SIZE):
            animals.remove(animals[-1])
