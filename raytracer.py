#Oscar Fernando López Barrios
#Carné 20679
#Gráficas Por Computadora
#Proyecto 2

from math import *
from sphere import *
from vector import *
from gl import *
from material import *
from light import *
from color import *

max_recursion_depth = 3

def refraction_objeto(I, N, roi):
    eta_i = 1
    eta_t = roi

    cos_i = ((I @ N) * -1)

    if cos_i < 0:
        cos_i *= -1
        eta_i *= -1
        eta_t *= -1
        N *= -1

    if eta_t == 0:
        eta_t = 1e-06

    eta = eta_i / eta_t

    k = (1 - (eta ** 2)) * (1 - (cos_i ** 2))

    if k < 0:
        return V3(0, 0, 0)

    cos_t = k ** 0.5

    return ((I * eta) + (N * ((eta * cos_i) - cos_t))).norm()

class RayTracer(object):

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.clear_color = Color(0, 0, 0)
        self.current_color = Color(1, 1, 1)
        self.scene = []
        self.light = None
        self.envmap = None
        self.clear()
    
    def clear(self):
        self.framebuffer = [
            [self.clear_color for x in range(self.width)]
            for y in range(self.height)
        ]
    
    def point(self, x, y, c = None):
        if y >= 0 and y < self.height and x > 0 and x < self.width:
            self.framebuffer[y][x] = c or self.current_color

    def write(self, filename):
        Render.glFinish(self, filename)

    def setBackground(self, background):
        self.envmap = background

    def render(self):
        fov = int(pi/2)
        ar = self.width / self.height
        tana = tan(fov / 2)
        for y in range(self.height):
            for x in range(self.width):
                i = ((2 * (x + 0.5) / self.width) - 1) * ar * tana
                j = (1 - (2 * (y + 0.5) / self.height)) * tana

                direction = V3(i, j, -1).norm()
                origin = V3(0, 0, 0)
                self.point(x, y, self.cast_ray(origin, direction))

    def cast_ray(self, origin, direction, recursion = 0):
        material, intersect = self.scene_intersect(origin, direction)

        if recursion == max_recursion_depth:
            if(self.envmap):
                 return self.envmap.getColor(direction)
            else:
                return self.clear_color

        if material is None:
            if(self.envmap):
                return self.envmap.getColor(direction)
            else:
                return self.clear_color

        light_direction = (self.light.position - intersect.point).norm()
        intensity = light_direction @ intersect.normal
        
        shadow_bias = 1.1
        shadow_origin = intersect.point + (intersect.normal * shadow_bias)
        shadow_material, material_intersect = self.scene_intersect(shadow_origin, light_direction)
        shadow_intensity = 0

        if shadow_material:
            shadow_intensity = 0.3

        diffuse = material.diffuse * intensity * material.albedo[0] * (1 - shadow_intensity)


        light_reflection = (light_direction - (intersect.normal) * (2 * intensity)).norm()
        specular_intensity = self.light.intensity * (max(0, (light_reflection @ direction)) ** material.spec)
        specular = self.light.c * specular_intensity * material.albedo[1]

        if material.albedo[2] > 0:
            reverse_direction = direction * -1
            reflection_direction = (light_direction - (intersect.normal) * (2 * (reverse_direction @ intersect.normal))).norm()
            reflection_origin = intersect.point + (intersect.normal * 1.1)
            reflection_color = self.cast_ray(reflection_origin, reflection_direction, recursion + 1)
        else:
            reflection_color = Color(0, 0, 0)

        if material.albedo[3] > 0:
            refraction_direction = refraction_objeto(direction, intersect.normal, material.refractive)
            refraction_origin = intersect.point + (intersect.normal * 1.1)
            refraction_color = self.cast_ray(refraction_origin, refraction_direction, recursion + 1)
        else:
            refraction_color = Color(0, 0, 0)

        reflection = (reflection_color * material.albedo[2])
        refraction = (refraction_color * material.albedo[3])

        return diffuse + specular + reflection + refraction

    def scene_intersect(self, origin, direction):
        zBuffer = 999999
        material = None
        intersect = None

        for obj in self.scene:
            obj_intersect = obj.ray_intersect(origin, direction)
            if obj_intersect and obj_intersect.distance < zBuffer:
                zBuffer = obj_intersect.distance
                material = obj.material
                intersect = obj_intersect

        return material, intersect