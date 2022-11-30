#Oscar Fernando López Barrios
#Carné 20679
#Gráficas Por Computadora
#Proyecto 2

from triangle import * 

class Pyramid(object):
    def __init__(self, vertices, material):
        self.v1, self.v2, self.v3, self.v4 = vertices
        self.material = material
        self.triangles_list = self.triangles()

    def triangles(self):

        triangle_1 = Triangle((self.v1, self.v2, self.v3), self.material)
        triangle_2 = Triangle((self.v1, self.v2, self.v4), self.material)
        triangle_3 = Triangle((self.v1, self.v4, self.v3), self.material)
        triangle_4 = Triangle((self.v2, self.v4, self.v3), self.material)

        return [triangle_1, triangle_2, triangle_3, triangle_4]

    def ray_intersect(self, origin, direction):
        min_t = float('-inf')
        max_t = float('inf')

        intersect = None

        for triangle in self.triangles_list:
            intersect_triangle = triangle.ray_intersect(origin, direction)

            if intersect_triangle and intersect_triangle.distance < max_t:
                max_t = intersect_triangle.distance
                intersect = intersect_triangle
        
        return intersect