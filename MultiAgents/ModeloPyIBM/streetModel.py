# Importamos las clases que se requieren para manejar los agentes (Agent) y su entorno (model).
# Cada model puede contener múltiples agentes.
from mesa import Agent, Model

# Debido a que necesitamos que existe un solo agente por celda, elegimos ''MultiGrid''.
from mesa.space import MultiGrid

# Con ''SimultaneousActivation, hacemos que todos los agentes se activen ''al mismo tiempo''.
from mesa.time import SimultaneousActivation

# Haremos uso de ''DataCollector'' para obtener información de cada paso de la simulación.
from mesa.datacollection import DataCollector

# Importamos los siguientes paquetes para el mejor manejo de valores numéricos.
import numpy as np
import pandas as pd
import random

def get_grid(model):
    grid = np.zeros( (model.grid.width, model.grid.height) )
    for (content, x, y) in model.grid.coord_iter():
        for contenido in content:
            if isinstance(contenido, CarAgent):
                """
                if contenido.direction == 0:
                    grid[x][y] = -0.9
                if contenido.direction == 1:
                    grid[x][y] = -0.8
                if contenido.direction == 2:
                    grid[x][y] = -0.5
                if contenido.direction == 3:
                    grid[x][y] = -0.3
                """
                grid[x][y] = contenido.unique_id
            elif isinstance(contenido, LightAgent):
                if contenido.state == 0:
                    grid[x][y] = 41
                else:
                    grid[x][y] = 42
            
            else:
                grid[x][y] = 0.4 #SEMAFORO
                
    return grid

class CarAgent(Agent):
    N = 0
    W = 1
    S = 2
    E = 3
    
    right = 1
    left = 2
    front = 3
    
    def __init__(self, unique_id, model, pos, direction, where_to_go):
        super().__init__(unique_id, model)
        self.x, self.y = pos
        self.move_to = None #where to move to
        self.has_passed = False
        self.direction = direction
        self.where_to_go = where_to_go
        self.my_light = ""
        self.unique_id = unique_id
    
    def step(self):
        turn = False
        neighbours = self.model.grid.get_neighbors(self.pos, moore=True, include_center=True)
        
        if self.direction == 0:
            self.my_light = "north"
            
            if self.lookCar() == False:
            
                if self.y == 9 or self.x == 9 or self.y == 0:
                    self.model.light_north -= 1
                    self.model.kill_agents.append(self)

                if self.x == 3:
                    if self.lookLight() == True:
                        self.x += 1
                    else:
                        self.x += 0 #Este debe ser 0


                else:
                    if self.where_to_go == 1:# DERECHA
                        if self.x == 4:
                            self.y -= 1
                        else:
                            self.x += 1

                    elif self.where_to_go == 2:
                        if self.x == 5:
                            self.y += 1
                        else:
                            self.x += 1

                    else:
                        self.x += 1

#-------------------------------------------------------------------------------------------------------------------------------

        elif self.direction == 1:
            self.my_light = "west"
            
            if self.lookCar() == False:
            
                if self.y == 9 or self.x == 0 or self.x == 9:
                    self.model.light_west -= 1
                    self.model.kill_agents.append(self)

                if self.y == 3:
                    if self.lookLight() == True:
                        self.y += 1
                    else:
                        self.y += 0 #Este debe ser 0            

                else:
                    if self.where_to_go == 1: # DERECHA
                        if self.y == 4:
                            self.x += 1
                        else:
                            self.y += 1

                    elif self.where_to_go == 2:
                        if self.y == 5:
                            self.x -= 1
                        else:
                            self.y += 1

                    else:
                        self.y += 1
                
#-------------------------------------------------------------------------------------------------------------------------------

        elif self.direction == 2:
            self.my_light = "south"
            
            if self.lookCar() == False:
                
                if self.y == 0 or self.x == 0 or self.y == 9:
                    self.model.light_south -= 1
                    self.model.kill_agents.append(self)
                    
                if self.x == 6:
                    if self.lookLight() == True:
                        self.x -= 1
                    else:
                        self.x -= 0 #Este debe ser 0
                else:
                    if self.where_to_go == 1: # DERECHA
                        if self.x == 5:
                            self.y += 1
                        else:
                            self.x -= 1

                    elif self.where_to_go == 2:
                        if self.x == 4:
                            self.y -= 1
                        else:
                            self.x -= 1

                    else:
                        self.x -= 1
                
#-------------------------------------------------------------------------------------------------------------------------------

        elif self.direction == 3:
            self.my_light = "east"
            
            if self.lookCar() == False:
                
                if self.y == 0 or self.x == 0 or self.x == 9:
                    self.model.light_east -= 1
                    self.model.kill_agents.append(self)
            
                if self.y == 6:
                    if self.lookLight() == True:
                        
                        self.y -= 1
                    else:
                        self.y -= 0 #Este debe ser 0

                else:
                    if self.where_to_go == 1: # DERECHA
                        if self.y == 5:
                            self.x -= 1
                        else:
                            self.y -= 1

                    elif self.where_to_go == 2:
                        if self.y == 4:
                            self.x += 1
                        else:
                            self.y -= 1

                    else:
                        self.y -= 1
        
        #print("(",self.x,",", self.y,")")
        self.move_to = self.x, self.y
        self.model.grid.move_agent(self, self.move_to)
        
    def lookLight(self):
        neighbours = self.model.grid.get_neighbors(self.pos, moore=True, include_center=True)
        for neighbor in neighbours:
            if isinstance(neighbor, LightAgent):
                if neighbor.state == neighbor.RED:
                    return False
                else:
                    return True
                
    def lookCar(self):
        if self.direction == 0 and self.y == 4: #NORTH
            neighbours = self.model.grid.get_neighbors(self.pos, moore = False, include_center = False)
            for neighbour in neighbours:
                if isinstance(neighbour, CarAgent) and neighbour.pos == (self.x + 1, self.y):
                    return True
                
        elif self.direction == 1: #WEST
            if self.x == 5:
                neighbours = self.model.grid.get_neighbors(self.pos, moore = False, include_center = False)
                for neighbour in neighbours:
                    if isinstance(neighbour, CarAgent) and neighbour.pos == (self.x, self.y + 1):
                        return True
        
        elif self.direction == 2 and self.y == 5:#SOUTH
                neighbours = self.model.grid.get_neighbors(self.pos, moore = False, include_center = False)
                for neighbour in neighbours:
                    if isinstance(neighbour, CarAgent) and neighbour.pos == (self.x - 1, self.y):
                        return True
        
        elif self.direction == 3: #EAST
            if self.x == 4:
                neighbours = self.model.grid.get_neighbors(self.pos, moore = False, include_center = False)
                for neighbour in neighbours:
                    if isinstance(neighbour, CarAgent) and neighbour.pos == (self.x, self.y - 1):
                        return True
        
        return False

""" Este agente es el agente de las cajas """
class LightAgent(Agent):
    GREEN = 1
    RED = 0
    
    def __init__(self, id_unique, pos_light, model, state = RED):
        super().__init__(pos_light, model)
        self.x, self.y = pos_light
        self.state = state
        self.cont_carros = 0
        
    def step(self):

        if self.x == 6 and self.y == 6:#SOUTH
            if self.weightLight() == "south":
                self.state = self.GREEN
            else:
                self.state = self.RED
            
        elif self.x == 3 and self.y == 6: #EAST
            if self.weightLight() == "east":
                self.state = self.GREEN
            else:
                self.state = self.RED
            
        elif self.x == 3 and self.y == 3:#NORTH
            if self.weightLight() == "north":
                self.state = self.GREEN
            else:
                self.state = self.RED
            
        elif self.x == 6 and self.y == 3:#WEST
            if self.weightLight() == "west":
                self.state = self.GREEN
            else:
                self.state = self.RED
            
            
    def weightLight(self):
        
        if(self.model.light_north > self.model.light_west and
              self.model.light_north > self.model.light_south and
              self.model.light_north > self.model.light_east):
            return "north"
        
        elif(self.model.light_west > self.model.light_north and
              self.model.light_west > self.model.light_south and
              self.model.light_west > self.model.light_east):
            return "west"
        
        elif(self.model.light_south > self.model.light_west and
              self.model.light_south > self.model.light_north and
              self.model.light_south > self.model.light_east):
            return "south"
        
        elif(self.model.light_east > self.model.light_west and
              self.model.light_east > self.model.light_north and
              self.model.light_east > self.model.light_south):
            return "east"
            
        
        elif(self.model.light_south == self.model.light_west or
              self.model.light_south == self.model.light_north or
              self.model.light_south == self.model.light_east):
            return "south"
        
        elif(self.model.light_north == self.model.light_west or
              self.model.light_north == self.model.light_south or
              self.model.light_north == self.model.light_east):
            return "north"
        
        elif(self.model.light_east == self.model.light_west or
              self.model.light_east  == self.model.light_south or
              self.model.light_east  == self.model.light_north):
            return "east"

        else:
            
            return "west"
        
class StreetModel(Model):
    def __init__(self, width, height, num_cars):
        self.num_cars = num_cars
        self.num_light = 4
        self.grid = MultiGrid(width, height, True)
        self.schedule = SimultaneousActivation(self)
        self.kill_agents = []
        self.light_north = 0
        self.light_west = 0
        self.light_south = 0
        self.light_east = 0
        self.i = 1
        
        """Repartimos los semaforos en los lugares ya especificados"""
        free_cells = list(self.grid.empties)
        for i in range(4):
            if i == 0:
                light1 = LightAgent("id" + str(i), (6,6), self)
                self.grid.place_agent(light1, (6,6)) #SEMAFORO SOUTH
                self.schedule.add(light1)
                                  
            elif i == 1:
                light = LightAgent("id" + str(i), (3,6),self)
                self.grid.place_agent(light, (3,6)) #SEMAFORO EAST
                self.schedule.add(light)
                                  
            elif i == 2:
                light = LightAgent("id" + str(i), (3,3),self)
                self.grid.place_agent(light, (3,3)) #SEMAFORO NORTH
                self.schedule.add(light)
            
            elif i == 3:
                light = LightAgent("id" + str(i), (6,3),self)
                self.grid.place_agent(light, (6,3)) #SEMAFORO WEST
                self.schedule.add(light)
        #self.datacollector = DataCollector(model_reporters = {'Grid': get_grid})

    def step(self, num_autos):
        """ Ejecuta un paso de la simulación."""
        if self.i < num_autos:
            
            choice = random.randint(0, 2)
            dir_ = 3
            
            N = 0
            W = 1
            S = 2
            E = 3
            
            right = 1
            left = 2
            front = 3
            
            if choice == 0:
                dir_ = right
            elif choice == 1:
                dir_ = left
            elif choice == 2:
                dir_ = front

            if self.i%4 == 0:
                car = CarAgent(self.i, self, (0, 4), N, dir_)
                self.grid.place_agent(car, (0, 4)) #CARROS DEL NORTE
                self.schedule.add(car)
                self.light_north += 1
                                  
            elif self.i%4 == 1:
                car = CarAgent(self.i, self, (5, 0), W, dir_)
                self.grid.place_agent(car, (5, 0)) #CARROS DEL OESTE
                self.schedule.add(car)
                self.light_west += 1
                                  
            elif self.i%4 == 2:
                car = CarAgent(self.i, self, (9, 5), S, dir_)
                self.grid.place_agent(car, (9, 5)) #CARROS DEL SUR
                self.schedule.add(car)
                self.light_south += 1
            
            elif self.i%4 == 3:
                car = CarAgent(self.i, self, (4, 9), E, dir_)
                self.grid.place_agent(car, (4, 9)) #CARRO DEL ESTE
                self.schedule.add(car)
                self.light_east += 1
        
        self.i += 1
        #self.datacollector.collect(self)
        self.schedule.step()
        for x in self.kill_agents:
            self.grid.remove_agent(x)
            self.schedule.remove(x)
            self.kill_agents.remove(x)