'''

'''

import random
import util_funcs as uf


def _mutate(pcolor, mutate_rate):
    
    cred, cgreen, cblue = pcolor
    
    if(random.random() > 1 - mutate_rate):
        cred = pcolor[0] + uf.randomly_add_or_sub() * 10
        if(cred < 0):
            cred = 0
        elif(cred > 255):
            cred = 255
    if(random.random() > 1 - mutate_rate):
        cgreen = pcolor[1] + uf.randomly_add_or_sub() * 10
        if(cgreen < 0):
            cgreen = 0
        elif(cgreen > 255):
            cgreen = 255
    if(random.random() > 1 - mutate_rate):
        cblue = pcolor[2] + uf.randomly_add_or_sub() * 10
        if(cblue < 0):
            cblue = 0
        elif(cblue > 255):
            cblue = 255

    return((cred, cgreen, cblue))


class Plant():
    
    def __init__(self, _xpos, _ypos, pcolor = (128, 128, 128),
                     PLANT_DISP_RADIUS = 35,
                     PLANT_REWARD_PER_STEP = 0.01,
                     PLANT_REPRODUCTION_THRESHOLD = 0.75,
                     PLANT_MUTATION_RATE = 0.5,
                     PLANT_SPREAD = 10,
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
            plant_population.append(Plant(self._xpos + uf.randomly_add_or_sub() * self.PLANT_SPREAD,
                                          self._ypos + uf.randomly_add_or_sub() * self.PLANT_SPREAD,
                                          _mutate(self.pcolor, self.PLANT_MUTATION_RATE)))
        
        if(self.fitness < self.PLANT_LOWER_THRESHOLD):
            plant_population.remove(self)
            del self
            
        self.fitness += self.PLANT_REWARD_PER_STEP


class Animal():
    pass
