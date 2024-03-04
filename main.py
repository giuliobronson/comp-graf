import numpy as np
import os

from helpers import get_rotation_matrix
from printer import Printer
from face import Face
from cube import Cube

if __name__ == "__main__":

    # Inicialização de faces quadradas
    f1 = Face([np.array((-0.5, 0.5, 0.5)), np.array((0.5, 0.5, 0.5)), np.array((0.5, -0.5, 0.5)), np.array((-0.5, -0.5, 0.5))])
    f2 = Face([np.array((0.5, 0.5, 0.5)), np.array((0.5, 0.5, -0.5)), np.array((0.5, -0.5, -0.5)), np.array((0.5, -0.5, 0.5))])
    f5 = Face([np.array((-0.5, 0.5, -0.5)), np.array((0.5, 0.5, -0.5)), np.array((0.5, 0.5, 0.5)), np.array((-0.5, 0.5, 0.5))])
    f3 = Face([np.array((0.5, 0.5, -0.5)), np.array((-0.5, 0.5, -0.5)), np.array((-0.5, -0.5, -0.5)), np.array((0.5, -0.5, -0.5))])
    f4 = Face([np.array((-0.5, 0.5, -0.5)), np.array((-0.5, 0.5, 0.5)), np.array((-0.5, -0.5, 0.5)), np.array((-0.5, -0.5, -0.5))])
    f6 = Face([np.array((-0.5, -0.5, 0.5)), np.array((0.5, -0.5, 0.5)), np.array((0.5, -0.5, -0.5)), np.array((-0.5, -0.5, -0.5))])

    # Instanciação de um cubo
    cube = Cube([f1, f2, f3, f4, f5, f6])

    # Matriz de rotação
    rotation_matrix = get_rotation_matrix(5, 6, 2)

    # Desenho do cubo
    printer = Printer("cube.txt")
    printer.play_rotation(cube, rotation_matrix)
    