from math import *
from sphere import *
from vector import *
from gl import *
from material import *
from light import *
from color import *

max_recursion_depth = 3

class RayTracer(object):

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.clear_color = Color(0, 0, 0)
        self.current_color = Color(1, 1, 1)
        self.scene = []
        self.light = None
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
            return self.clear_color

        if material is None:
            return self.clear_color

        light_direction = (self.light.position - intersect.point).norm()
        intensity = light_direction @ intersect.normal
        
        shade_blast = 1.1
        shade_origin = intersect.point + (intersect.normal * shade_blast)
        shade_material, material_intersect = self.scene_intersect(shade_origin, light_direction)
        shade_intensity = 0

        if shade_material:
            shade_intensity = 0.3

        diffuse = material.diffuse * intensity * material.albedo[0] * (1 - shade_intensity)


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

        reflection = reflection_color * material.albedo[2]

        return diffuse + specular + reflection

    def scene_intersect(self, origin, direction):
        zBuffer = 999999
        material = None
        intersect = None

        for obj in self.scene:
            obj_intersect = obj.ray_intersect(origin, direction)
            if obj_intersect:
                if obj_intersect.distance < zBuffer:
                    zBuffer = obj_intersect.distance
                    material = obj.material
                    intersect = obj_intersect

        return material, intersect