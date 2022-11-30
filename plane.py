#Oscar Fernando López Barrios
#Carné 20679
#Gráficas Por Computadora
#Proyecto 2

from intersect import *
from vector import *

class Plane(object):
    def __init__(self, center, width, large, material):
        self.center = center
        self.width = width
        self.large = large
        self.material = material
        
    def ray_intersect(self, origin, direction):

        if (direction.y == 0):
            direction.y = 1E-06
            
        d = (origin.y + self.center.y) / direction.y
        impact = origin + (direction * d)
        normal = V3(0, 1, 0)
        
        if (d <= 0) or \
            impact.x > (self.center.x + self.width / 2) or impact.x < (self.center.x - self.width / 2) or \
            impact.z > (self.center.z + self.large / 2) or impact.z < (self.center.z - self.large / 2): 
            return None
        
        return Intersect(
            distance=d,
            point=impact,
            normal=normal
        )