from material import *
from sphere import *
from vector import *
from raytracer import *
from color import *

red = Material(difusse=Color(255, 0, 0), albedo = [1.3, 0.1, 0], spec = 50)
white = Material(difusse=Color(255, 255, 255), albedo = [1.3, 0.1, 0], spec = 40)
orange = Material(difusse=Color(255, 165, 0), albedo = [1.3, 0.1, 0], spec = 50)
black = Material(difusse=Color(0, 0, 0), albedo = [1.3, 0.1, 0], spec = 50)
silver = Material(difusse=Color(192, 192, 192), albedo = [1.3, 0.1, 0], spec = 50)
light_brown = Material(difusse=Color(204, 102, 53), albedo = [1.3, 0.1, 0], spec = 30)
apricot = Material(difusse=Color(242, 178, 140), albedo = [1.3, 0.1, 0], spec = 30)


r = RayTracer(1024, 1024)
r.light = Light(V3(0, 0, 0), 1, Color(255, 255, 255))
r.scene = [
    
    #Cuerpo Oso 1
    Sphere(V3(-2.5, -0.4, -8), 0.4, white),
    Sphere(V3(-1.5, -0.4, -8), 0.4, white),
    Sphere(V3(-2, 0, -8), 0.7, silver),
    Sphere(V3(-2.5, 0.5, -8), 0.4, white),
    Sphere(V3(-1.5, 0.5, -8), 0.4, white),
    Sphere(V3(-2, -0.9, -8), 0.5, white),

    #Ojos y Nariz Oso 1
    Sphere(V3(-1.95, -0.85, -7), 0.08, black),
    Sphere(V3(-1.6, -0.85, -7), 0.08, black),
    Sphere(V3(-1.77, -0.75, -7), 0.06, black),

    #Orejas Oso 1
    Sphere(V3(-2.5, -1.3, -8), 0.3, white),
    Sphere(V3(-1.5, -1.3, -8), 0.3, white),



    #Cuerpo Oso 2
    Sphere(V3(2.5, -0.4, -8), 0.4, apricot),
    Sphere(V3(1.5, -0.4, -8), 0.4, apricot),
    Sphere(V3(2, 0, -8), 0.7, red),
    Sphere(V3(2.5, 0.5, -8), 0.4, apricot),
    Sphere(V3(1.5, 0.5, -8), 0.4, apricot),
    Sphere(V3(2, -0.9, -8), 0.5, apricot),

    #Ojos y Nariz Oso 2
    Sphere(V3(1.95, -0.85, -7), 0.08, black),
    Sphere(V3(1.6, -0.85, -7), 0.08, black),
    Sphere(V3(1.77, -0.75, -7), 0.1, light_brown),
    Sphere(V3(1.52, -0.65, -6), 0.04, black),

    #Orejas Oso 2
    Sphere(V3(2.5, -1.3, -8), 0.3, light_brown),
    Sphere(V3(1.5, -1.3, -8), 0.3, light_brown),

]
r.render()
r.write('RT2.bmp')