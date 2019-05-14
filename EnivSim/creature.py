'''

'''

import random
import util_funcs as uf

width = 500
height = 500

PLANT_DISP_RADIUS = width * 0.07
PLANT_REWARD_PER_STEP = 0.01
PLANT_REPRODUCTION_THRESHOLD = 0.75
PLANT_MUTATION_RATE = 0.1
PLANT_SPREAD = 10
PLANT_LOWER_THRESHOLD = 0.2


def _mutate(pcolor, mutate_rate):
    
    cred, cgreen, cblue = pcolor
    
    if(random.random() > 1 - mutate_rate):
        cred = pcolor[0] + uf.randomly_add_or_sub() * 4
    if(random.random() > 1 - mutate_rate):
        cgreen = pcolor[1] + uf.randomly_add_or_sub() * 4
    if(random.random() > 1 - mutate_rate):
        cblue = pcolor[2] + uf.randomly_add_or_sub() * 4

    return((cred, cgreen, cblue))

class Plant():
    
    def __init__(self, pcolor = (128, 128, 128),
                     _xpos = width/2, _ypos = height/2):
        
        self.fitness = 0.5
        self.pcolor = pcolor
        
        self._xpos = _xpos
        self._ypos = _ypos
        
        
    def render(self):
        fill(self.pcolor[0], self.pcolor[1], self.pcolor[2],
             int(self.fitness * 255))
        radius = PLANT_DISP_RADIUS * self.fitness
        ellipse(self._xpos, self._ypos, radius, radius)
        
    def update_time_step(self, plant_population):
        
        if(self.fitness > PLANT_REPRODUCTION_THRESHOLD):
            plant_population.append(Plant(_mutate(self.pcolor, PLANT_MUTATION_RATE),
                                          self._xpos + uf.randomly_add_or_sub() * PLANT_SPREAD,
                                          self._ypos + uf.randomly_add_or_sub() * PLANT_SPREAD))
        
        if(self.fitness < PLANT_LOWER_THRESHOLD):
            plant_population.remove(self)
            del self
            
        self.fitness += PLANT_REWARD_PER_STEP


class Animal():
    pass
