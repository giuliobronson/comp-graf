class Polyhedron:

    def __init__(self, faces):
        self.faces = faces

    def rotate(self, rotation_matrix):
        for face in self.faces:
            face.rotate(rotation_matrix)
            