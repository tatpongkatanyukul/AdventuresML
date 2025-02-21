from matplotlib import pyplot as plt
import numpy as np

def vec2plot(vec, arrow_size=0.2, arrow_angle=20):
    '''
    Compute positions of arrow draw from a vector.
    arrow_size: length of arrow head
    arrow_angle: a relative angle to the vector (in degree).
    '''
    assert len(vec) == 2

    # Convert degree to radian
    arrow_angle = arrow_angle/180 * np.pi

    xplt, yplt = np.array([0, vec[0]]), np.array([0, vec[1]])

    vecangle = np.float64(np.pi/2)

    er = 1e-4
    if abs(vec[0]) > er:
        vecangle = np.arctan(vec[1]/vec[0])

    if vec[0] < 0:
        vecangle += np.pi

    # arrow absolute angles
    # abs_angles = vecangle + [np.pi/2, -np.pi/2]
    abs_angles = vecangle + [np.pi - arrow_angle, arrow_angle - np.pi ]

    arrow_dx = arrow_size * np.cos(abs_angles)
    arrow_dy = arrow_size * np.sin(abs_angles)

    # arrow head drawing positions
    arrow_x = vec[0] + arrow_dx
    arrow_y = vec[1] + arrow_dy

    # Put drawing positions in order
    arrow_points_x = [arrow_x[0], vec[0], arrow_x[1]]
    arrow_points_y = [arrow_y[0], vec[1], arrow_y[1]]

    return xplt, yplt, arrow_points_x, arrow_points_y

if __name__ == '__main__':
    v = np.array([3,4])
    x, y, arr_x, arr_y = vec2plot(v)
    plt.plot(x, y, 'red')
    plt.plot(arr_x, arr_y, 'blue')
    plt.axes().set_aspect('equal')
    plt.show()

