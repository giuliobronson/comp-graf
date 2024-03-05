import numpy as np
import os

class Printer:

    def __init__(self, file_name):
        if os.path.exists(file_name):
            os.remove(file_name)

        self.file_name = file_name

    def draw_line(self, p1, p2):
        return f"line\n {p1[0]} {p1[1]} {p2[0]} {p2[1]}\n"
    
    def clear_screen(self):
        with open(f"{self.file_name}", "a") as file:
            file.write("clrscr\n")

    def print(self, object, z=0, f=0, occlusion=False, delay=0.1):
        with open(f"{self.file_name}", "a") as file:
            for face in object.faces:
                for i, _ in enumerate(face.points):
                    lenght = len(face.points)
                    p1 = face.points[i]
                    p2 = face.points[(i + 1) % lenght]
                    v = np.array([0, 0, 1])
                    if f != 0:                        
                        p1 = (p1[0] * f / (z + p1[2]), p1[1] * f / (z + p1[2]), z)
                        p2 = (p2[0] * f / (z + p2[2]), p2[1] * f / (z + p2[2]), z)
                        v = -np.array(p1)
                    if occlusion == True:
                        prod = np.transpose(face.normal_vector) @ v
                        if prod > 0:
                            file.write(self.draw_line(p1, p2))
                    else:
                        file.write(self.draw_line(p1, p2))
            
            file.write(f"delay\n{delay}\n")

    def play_rotation(self, object, rotation_matrix, z=0, f=0, occlusion=False, iterations=100):
        for _ in range (0, iterations):
            self.print(object, z=z, f=f, occlusion=occlusion)
            self.clear_screen()
            object.rotate(rotation_matrix)

        os.system(f".\winplot.exe {self.file_name}")
