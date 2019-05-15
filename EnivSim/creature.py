
import random
import util_funcs as uf

class Plant():
    
    def __init__(self, _xpos, _ypos, pcolor = (128, 128, 128),
                     PLANT_DISP_RADIUS = 35,
                     PLANT_REWARD_PER_STEP = 0.01,
                     PLANT_REPRODUCTION_THRESHOLD = 0.8,
                     PLANT_MUTATION_RATE = 1,
                     PLANT_SPREAD = 200,
                     PLANT_LOWER_THRESHOLD = 0.2):
        
        self.fitness = 0.5
        self.pcolor = pcolor
        
        self._xpos = _xpos
        self._ypos = _ypos
        
        self.PLANT_DISP_RADIUS = PLANT_DISP_RADIUS
        self.PLANT_REWARD_PER_STEP = PLANT_REWARD_PER_STEP
        self.PLANT_REPRODUCTION_THRESHOLD = PLANT_REPRODUCTION_THRESHOLD
        self.PLANT_MUTATION_RATE = PLANT_MUTATION_RATE
        self.PLANT_SPREAD = PLANT_SPREAD
        self.PLANT_LOWER_THRESHOLD = PLANT_LOWER_THRESHOLD
        
    def render(self):
        fill(self.pcolor[0], self.pcolor[1], self.pcolor[2],
             int(self.fitness * 255))
        radius = self.PLANT_DISP_RADIUS * self.fitness
        ellipse(self._xpos, self._ypos, radius, radius)
        
    def update_time_step(self, plant_population):
        
        if(self.fitness > self.PLANT_REPRODUCTION_THRESHOLD):
            plant_population.append(Plant(uf.plant_spread_pos(self, self._xpos, 'w'),
                                          uf.plant_spread_pos(self, self._ypos, 'h'),
                                          uf._mutate(self.pcolor, self.PLANT_MUTATION_RATE)))
            self.fitness -= 0.5
            self.PLANT_LOWER_THRESHOLD += 0.05
        
        if(self.fitness < self.PLANT_LOWER_THRESHOLD):
            plant_population.remove(self)
            del self
            return(None)
        
        self.PLANT_LOWER_THRESHOLD += 0.001
        
        if(self.fitness < 1):
            self.fitness += self.PLANT_REWARD_PER_STEP



class Animal():

    def __init__(self, _xpos, _ypos, pcolor = (128, 128, 128),
                     ANIMAL_DISP_LENGTH = 35,
                     ANIMAL_COST_PER_STEP = 0.0025,
                     ANIMAL_REWARD_PER_FOOD = 0.05,
                     ANIMAL_EATING_RADIUS = 10,
                     ANIMAL_SPEED = 3,
                     ANIMAL_REPRODUCTION_THRESHOLD = 0.85,
                     ANIMAL_MUTATION_RATE = 0.5,
                     ANIMAL_SPREAD = 10,
                     ANIMAL_LOWER_THRESHOLD = 0.2):
        
        self.fitness = 0.5
        self.pcolor = pcolor
        
        self._xpos = _xpos
        self._ypos = _ypos
        
        self.ANIMAL_DISP_LENGTH = ANIMAL_DISP_LENGTH
        self.ANIMAL_COST_PER_STEP = ANIMAL_COST_PER_STEP
        self.ANIMAL_REWARD_PER_FOOD = ANIMAL_REWARD_PER_FOOD
        self.ANIMAL_EATING_RADIUS = ANIMAL_EATING_RADIUS
        self.ANIMAL_SPEED = ANIMAL_SPEED
        self.ANIMAL_REPRODUCTION_THRESHOLD = ANIMAL_REPRODUCTION_THRESHOLD
        self.ANIMAL_MUTATION_RATE = ANIMAL_MUTATION_RATE
        self.ANIMAL_SPREAD = ANIMAL_SPREAD
        self.ANIMAL_LOWER_THRESHOLD = ANIMAL_LOWER_THRESHOLD
        
    def render(self):
        fill(self.pcolor[0], self.pcolor[1], self.pcolor[2],
             int(self.fitness * 255))
        dlength = self.ANIMAL_DISP_LENGTH * self.fitness
        rectMode(CENTER)
        rect(self._xpos, self._ypos, dlength, dlength)
        
    def update_time_step(self, animal_population, plant_population):
        if(self.fitness > self.ANIMAL_REPRODUCTION_THRESHOLD):
            animal_population.append(Animal(self._xpos,
                                          self._ypos,
                                          uf._mutate(self.pcolor, self.ANIMAL_MUTATION_RATE)))
            self.fitness -= 0.5
            self.ANIMAL_LOWER_THRESHOLD += 0.05
        
        if(self.fitness < self.ANIMAL_LOWER_THRESHOLD):
            animal_population.remove(self)
            del self
            return(None)
        
        self._move(plant_population)
        
    def _move(self, plant_population):
        
        self.ANIMAL_LOWER_THRESHOLD += 0.001
        if(self.fitness > 0):
            self.fitness -= self.ANIMAL_COST_PER_STEP
            
        if(len(plant_population) == 0):
            return(None)
            
        plant_distance = [uf.distance(self, plant) for plant in plant_population]
        
        closest_plant_index = plant_distance.index(min(plant_distance))
        closest_plant = plant_population[closest_plant_index]
        
        self._xpos += self.ANIMAL_SPEED if ((closest_plant._xpos - self._xpos) > 0) else -self.ANIMAL_SPEED
        self._ypos += self.ANIMAL_SPEED if ((closest_plant._ypos - self._ypos) > 0) else -self.ANIMAL_SPEED


        if(plant_distance[closest_plant_index] < self.ANIMAL_EATING_RADIUS):
            if(self.fitness < 1):
                self.fitness += self.ANIMAL_REWARD_PER_FOOD
            closest_plant.fitness -= self.ANIMAL_REWARD_PER_FOOD
            
