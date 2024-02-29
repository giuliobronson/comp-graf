import numpy as np
from face import Face
from cube import Cube

if __name__ == "__main__":
    f1 = Face(np.array((-1, 1, 1)), np.array((1, 1, 1)), np.array((1, -1, 1)), np.array((-1, -1, 1)))
    f2 = Face(np.array((1, 1, 1)), np.array((1, 1, -1)), np.array((1, -1, -1)), np.array((1, -1, 1)))
    f3 = Face(np.array((1, 1, -1)), np.array((-1, 1, -1)), np.array((-1, -1, -1)), np.array((1, -1, -1)))
    f4 = Face(np.array((-1, 1, -1)), np.array((-1, 1, 1)), np.array((-1, -1, 1)), np.array((-1, -1, -1)))
    f5 = Face(np.array((-1, 1, -1)), np.array((1, 1, -1)), np.array((1, 1, 1)), np.array((-1, 1, 1)))
    f6 = Face(np.array((-1, -1, 1)), np.array((1, -1, 1)), np.array((1, -1, -1)), np.array((-1, -1, -1)))