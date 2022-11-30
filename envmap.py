#Oscar Fernando López Barrios
#Carné 20679
#Gráficas Por Computadora
#Proyecto 2

import struct
from color import *
from math import *

class Envmap(object):
    def __init__(self, path):
        self.path = path
        self.read()
        
    def read(self):
        with open(self.path, "rb") as image:
            image.seek(10)
            header_size = struct.unpack("=l", image.read(4))[0]    
            image.seek(18)
            self.width = struct.unpack("=l", image.read(4))[0]    
            self.height = struct.unpack("=l", image.read(4))[0]    
            
            image.seek(header_size)
            
            self.pixels = []
            for y in range(self.height):
                self.pixels.append([])

                for x in range(self.width):
                    b = ord(image.read(1))
                    g = ord(image.read(1))
                    r = ord(image.read(1))
                    
                    self.pixels[y].append(
                        Color(r, g, b)
                    )
    
    def getColor(self, direction):

        normalized_direction = direction.norm()
        
        x = round(((atan2(normalized_direction.z, normalized_direction.x) / (2 * pi)) + 0.5) * self.width)
        y = (-1 * round((acos((-1 * normalized_direction.y)) / pi) * self.height))

        x -= 1 if (x > 0) else 0
        y -= 1 if (y > 0) else 0

        return self.pixels[y][x]