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
from plane import *
from envmap import *

#Materiales
red_ball = Material(difusse=Color(255, 0, 0), albedo = [1, 0.1, 0.48, 0], spec = 50, refractive=50)
yellow_ball = Material(difusse=Color(249,236,12), albedo = [1, 0.1, 0.48, 0], spec = 50, refractive=50) 
white = Material(difusse=Color(255, 255, 255), albedo = [1.3, 0.1, 0, 0], spec = 40, refractive=20)
black = Material(difusse=Color(0, 0, 0), albedo = [1.3, 0.1, 0, 0], spec = 50, refractive=20)
light_brown = Material(difusse=Color(204, 102, 53), albedo = [1, 0.2, 0.2, 0], spec = 50, refractive=50)
apricot = Material(difusse=Color(242, 178, 140), albedo = [1, 0.1, 0.3, 0], spec = 50, refractive=50)
tree_leaves = Material(difusse=Color(2,105,57), albedo=[1, 0.1, 0, 0], spec=50, refractive=50)
tree_log = Material(difusse=Color(108,66,39), albedo=[1, 0.1, 0, 0], spec=50, refractive=50)

#Creacion de escena
r = RayTracer(1024, 1024)
r.light = Light(V3(0, 0, 0), 1, Color(255, 255, 255))
r.setBackground(Envmap('./background.bmp'))

#Carga de objetos
r.scene = [
    
    #Arbol
    Pyramid((V3(-4.5, 0, -10), V3(0, 0, -9), V3(-1.5, -1, -9), V3(-3, 0, -9)), tree_leaves),
    Pyramid((V3(-4.5, 1, -10), V3(1, 1, -9), V3(-1.5, -0.5, -9), V3(-4, 1, -9)), tree_leaves),
    Pyramid((V3(-4.5, 2.5, -10), V3(2, 2.5, -9), V3(-1.5, 0.5, -9), V3(-5, 2.5, -9)), tree_leaves),
    Cube(V3(-1.5, 2.98, -9), 1, tree_log),

    #Esferas
    Sphere(V3(-2.7, 0, -8), 0.25, red_ball),
    Sphere(V3(0, 0, -8), 0.25, yellow_ball),
    Sphere(V3(1, 1, -8), 0.25, red_ball),
    Sphere(V3(-3.6, 1, -8), 0.25, yellow_ball),
    Sphere(V3(1.7, 2.3, -8), 0.25, yellow_ball),
    Sphere(V3(-4.3, 2.3, -8), 0.25, red_ball),

    #Piso
    Plane(V3(3.3, 5, -11), 3, 6, light_brown),
    Plane(V3(0, 5, -11), 3, 6, light_brown),
    Plane(V3(-3.3, 5, -11), 3, 6, light_brown),

    #Regalo
    Cube(V3(1.23, 1.5, -4), 0.2, red_ball),
    Cube(V3(1.5, 2.2, -5), 0.5, apricot),

]
r.render()
r.write('Proyecto_2.bmp')