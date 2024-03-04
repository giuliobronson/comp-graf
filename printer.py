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

    def print(self, object, delay=0.1):
        with open(f"{self.file_name}", "a") as file:
            for face in object.faces:
                for i, _ in enumerate(face.points):
                    if i == 0: continue
                    file.write(self.draw_line(face.points[i - 1], face.points[i]))
            
            file.write(f"delay\n{delay}\n")

    def play_rotation(self, object, rotation_matrix, iterations=100):
        for _ in range (0, iterations):
            self.print(object)
            self.clear_screen()
            object.rotate(rotation_matrix)

        os.system(f"./plot {self.file_name}")
