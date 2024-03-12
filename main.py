import numpy as np
import os

from helpers import get_rotation_matrix
from printer import Printer
from face import Face
from polyhedron import Polyhedron

if __name__ == "__main__":

    # Inicialização de faces quadradas
    f1 = Face([np.array((-0.5, 0.5, 0.5)), np.array((0.5, 0.5, 0.5)), np.array((0.5, -0.5, 0.5)), np.array((-0.5, -0.5, 0.5))])
    f2 = Face([np.array((0.5, 0.5, 0.5)), np.array((0.5, 0.5, -0.5)), np.array((0.5, -0.5, -0.5)), np.array((0.5, -0.5, 0.5))])
    f5 = Face([np.array((-0.5, 0.5, -0.5)), np.array((0.5, 0.5, -0.5)), np.array((0.5, 0.5, 0.5)), np.array((-0.5, 0.5, 0.5))])
    f3 = Face([np.array((0.5, 0.5, -0.5)), np.array((-0.5, 0.5, -0.5)), np.array((-0.5, -0.5, -0.5)), np.array((0.5, -0.5, -0.5))])
    f4 = Face([np.array((-0.5, 0.5, -0.5)), np.array((-0.5, 0.5, 0.5)), np.array((-0.5, -0.5, 0.5)), np.array((-0.5, -0.5, -0.5))])
    f6 = Face([np.array((-0.5, -0.5, 0.5)), np.array((0.5, -0.5, 0.5)), np.array((0.5, -0.5, -0.5)), np.array((-0.5, -0.5, -0.5))])

    # # Instanciação de um cubo
    cube = Polyhedron([f1, f2, f3, f4, f5, f6])

    # Matriz de rotação
    rotation_matrix = get_rotation_matrix(5, 6, 2)
    cube.rotate(rotation_matrix)

    # Projeção ortogonal do cubo
    printer = Printer("./docs/cube1.txt")
    printer.print(cube, delay=3)

    # Projeção perspectiva do cubo
    printer = Printer("./docs/cube2.txt")
    printer.print(cube, z=2, f=1.8, delay=3)

    # Projeção ortogonal do cubo com oclusão
    printer = Printer("./docs/cube3.txt")
    printer.print(cube, occlusion=True, delay=3)

    # Projeção perspectiva do cubo
    printer = Printer("./docs/cube4.txt")
    printer.print(cube, z=2, f=1.8, occlusion=True, delay=3)

    # Rotação do primeiro cubo
    printer = Printer("./docs/rotation1.txt")
    printer.play_rotation(cube, rotation_matrix, z=0, f=0, occlusion=False)
    
    # Rotação do segundo cubo
    printer = Printer("./docs/rotation2.txt")
    printer.play_rotation(cube, rotation_matrix, z=2, f=1.8, occlusion=False)

     # Rotação do terceiro cubo
    printer = Printer("./docs/rotation3.txt")
    printer.play_rotation(cube, rotation_matrix, z=0, f=0, occlusion=True)
    
    # Rotação do quarto cubo
    printer = Printer("./docs/rotation4.txt")
    printer.play_rotation(cube, rotation_matrix, z=2, f=1.8, occlusion=True)
    