#Oscar Fernando López Barrios
#Carné 20679
#Gráficas Por Computadora
#Proyecto 2

from vector import *
from intersect import *

class Triangle(object):
  def __init__(self, vertices, material):
    self.v1, self.v2, self.v3  = vertices
    self.material = material

  def ray_intersect(self, origin, direction):

    side_1 = (self.v2 - self.v1)
    side_2 = (self.v3 - self.v1)

    vect = (direction * side_2)
    det = (side_1 @ vect)

    if (-1E-06 < det < 1E-06):
      return None

    det_inv = (1 / det)
    u = det_inv * ((origin - self.v1) @ vect)

    if ((u < 0) or (u > 1)):
      return None

    tvec = ((origin - self.v1) * side_1)
    v = det_inv * (direction @ tvec)

    if ((v < 0) or ((u + v) > 1)):
      return None

    qvec = det_inv * (side_2 @ tvec)

    if (qvec > 1E-06):

      impact = (origin + (direction * qvec))
      normal = (side_1 * side_2).norm()

      return Intersect(
        distance=qvec,
        point=impact,
        normal=normal,
      )

    else:
      return None