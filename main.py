#Oscar Fernando López Barrios
#Carné 20679
#Gráficas Por Computadora
#Proyecto 2

from material import *
from sphere import *
from vector import *
from raytracer import *
from color import *
from cube import *
from triangle import *

red = Material(difusse=Color(255, 0, 0), albedo = [1.3, 0.1, 0, 0], spec = 50, refractive=20)
white = Material(difusse=Color(255, 255, 255), albedo = [1.3, 0.1, 0, 0], spec = 40, refractive=20)
orange = Material(difusse=Color(255, 165, 0), albedo = [1.3, 0.1, 0, 0], spec = 50, refractive=20)
black = Material(difusse=Color(0, 0, 0), albedo = [1.3, 0.1, 0, 0], spec = 50, refractive=20)
silver = Material(difusse=Color(192, 192, 192), albedo = [1.3, 0.1, 0, 0], spec = 50, refractive=20)
light_brown = Material(difusse=Color(204, 102, 53), albedo = [1.3, 0.1, 0, 0], spec = 30, refractive=20)
apricot = Material(difusse=Color(242, 178, 140), albedo = [1.3, 0.1, 0, 0], spec = 30, refractive=20)


r = RayTracer(1024, 1024)
r.light = Light(V3(0, 0, 0), 1, Color(255, 255, 255))
r.scene = [
    
    Cube(V3(0, 1.8, -6.5), 0.6, silver),
    Triangle((V3(-4.5,0.5,-5),V3(-4.5,-0.45,-5),V3(-2,0.6,-5.5)),1,silver),

]
r.render()
r.write('Proyecto_2.bmp')