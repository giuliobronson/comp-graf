import numpy as np

def get_rotation_matrix(alpha, beta, theta):
    Rx = np.array([
        [1., 0., 0.],
        [0., np.cos(alpha * np.pi / 180), -np.sin(alpha * np.pi / 180)],
        [0., np.sin(alpha * np.pi / 180),  np.cos(alpha * np.pi / 180)]
    ])

    Ry = np.array([
        [ np.cos(beta * np.pi / 180), 0., np.sin(beta * np.pi / 180)],
        [0., 1., 0.],
        [-np.sin(beta * np.pi / 180), 0., np.cos(beta * np.pi / 180)]
    ])

    Rz = np.array([
        [np.cos(theta * np.pi / 180), -np.sin(theta * np.pi / 180), 0.],
        [np.sin(theta * np.pi / 180),  np.cos(theta * np.pi / 180), 0.],
        [0., 0., 1.]
    ])

    return np.round(Rx @ Ry @ Rz, 5)
    
    