import numpy as np

class Face:
    
    def __init__(self, p1, p2, p3, p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.normal_vector = np.cross(p4 - p1, p2 - p1)

    def rotate(self, rotation_matrix):
        self.p1 = rotation_matrix @ self.p1
        self.p2 = rotation_matrix @ self.p2
        self.p3 = rotation_matrix @ self.p3
        self.p4 = rotation_matrix @ self.p4