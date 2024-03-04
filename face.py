import numpy as np

class Face:
    
    def __init__(self, points):
        self.points = points
        self.normal_vector = np.cross(points[2] - points[1], points[1] - points[0])

    def rotate(self, rotation_matrix):
        for i, point in enumerate(self.points):
            self.points[i] = rotation_matrix @ point
        