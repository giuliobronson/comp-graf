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

    # Cubo com rotação e projeção ortogonal
    printer = Printer("cube_ort.txt")
    printer.play_rotation(cube, rotation_matrix, z=0, f=0, occlusion=False)
    
    # Cubo com rotação e projeção perspectiva
    printer = Printer("cube_pept.txt")
    printer.play_rotation(cube, rotation_matrix, z=2, f=1.5, occlusion=False)

     # Cubo com rotação e projeção ortogonal e oclusão
    printer = Printer("cube_ort_occ.txt")
    printer.play_rotation(cube, rotation_matrix, z=0, f=0, occlusion=True)
    
    # Cubo com rotação e projeção perspectiva e oclusão
    printer = Printer("cube_pept_occ.txt")
    printer.play_rotation(cube, rotation_matrix, z=2, f=1.5, occlusion=True)