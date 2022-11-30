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

  def ray_interception(self, origin, direction):

    edge_1 = (self.v2 - self.v1)
    edge_2 = (self.v3 - self.v1)

    height = (direction * edge_2)
    det = (edge_1 @ height)

    if (-1E-06 < det < 1E-06):
      return None

    tilt_inv = (1 / det)
    u = tilt_inv * ((origin - self.v1) @ height)

    if ((u < 0) or (u > 1)):
      return None

    tvec = ((origin - self.v1) * edge_1)
    v = tilt_inv * (direction @ qvec)

    if ((v < 0) or ((u + v) > 1)):
      return None

    qvec = tilt_inv * (edge_2 @ tvec)

    if (qvec > 1E-06):

      impact = (origin + (direction * tvec))
      normal = (edge_1 * edge_2).norm()

      return Intersect(
        distance=qvec,
        point=impact,
        normal=normal,
      )

    else:
      return None