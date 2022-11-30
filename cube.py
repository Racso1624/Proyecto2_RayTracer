#Oscar Fernando López Barrios
#Carné 20679
#Gráficas Por Computadora
#Proyecto 2

from intersect import *

class Cube(object): 
    def __init__(self, center, width_size, material):
        self.center = center
        self.width_size = width_size
        self.material = material

    def ray_intersect(self, origin, direction):
        min_t = float('-inf')
        max_t = float('inf')

        for i in range(3):
            if(direction.coords[i] != 0):
                min_t_coord = (((self.center.coords[i] - (self.width_size / 2)) - origin.coords[i]) / direction.coords[i])
                max_t_coord = (((self.center.coords[i] + (self.width_size / 2)) - origin.coords[i]) / direction.coords[i])

            if(min_t_coord > max_t_coord):
                min_t_coord, max_t_coord = max_t_coord, min_t_coord

            if(min_t_coord > min_t):
                min_t = min_t_coord
            
            if(max_t_coord < max_t):
                max_t = max_t_coord

            if(min_t > max_t):
                return None

        if(min_t < 0):
            min_t = max_t

            if(min_t < 0):
                return False

        impact = (direction * min_t) - origin
        normal = (impact - self.center).norm()

        return Intersect(
            distance = min_t, 
            point = impact, 
            normal = normal,
        )