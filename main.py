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
from pyramid import *
from envmap import *

red = Material(difusse=Color(255, 0, 0), albedo = [1.3, 0.1, 0, 0], spec = 50, refractive=20)
white = Material(difusse=Color(255, 255, 255), albedo = [1.3, 0.1, 0, 0], spec = 40, refractive=20)
orange = Material(difusse=Color(255, 165, 0), albedo = [1.3, 0.1, 0, 0], spec = 50, refractive=20)
black = Material(difusse=Color(0, 0, 0), albedo = [1.3, 0.1, 0, 0], spec = 50, refractive=20)
silver = Material(difusse=Color(192, 192, 192), albedo = [1.3, 0.1, 0, 0], spec = 50, refractive=20)
light_brown = Material(difusse=Color(204, 102, 53), albedo = [1.3, 0.1, 0, 0], spec = 30, refractive=20)
apricot = Material(difusse=Color(242, 178, 140), albedo = [1.3, 0.1, 0, 0], spec = 30, refractive=20)
tree_leaves = Material(difusse=Color(2,105,57), albedo=[1, 0.1, 0.3, 0], spec=50, refractive=50)
tree_log = Material(difusse=Color(108,66,39), albedo=[1, 0.1, 0.3, 0], spec=50, refractive=50)


r = RayTracer(1024, 1024)
r.light = Light(V3(0, 0, 0), 1, Color(255, 255, 255))
# r.setBackground(Envmap('./background.bmp'))
r.scene = [
    
    Pyramid((V3(-4.5, 0, -10), V3(0, 0, -9), V3(-1.5, -1, -9), V3(-3, 0, -9)), tree_leaves),
    Pyramid((V3(-4.5, 1, -10), V3(1, 1, -9), V3(-1.5, -0.5, -9), V3(-4, 1, -9)), tree_leaves),
    Pyramid((V3(-4.5, 2.5, -10), V3(2, 2.5, -9), V3(-1.5, 0.5, -9), V3(-5, 2.5, -9)), tree_leaves),
    Cube(V3(-1.5, 2.98, -9), 1, tree_log),

]
r.render()
r.write('Proyecto_2.bmp')