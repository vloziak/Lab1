import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

cube_vertices = np.array([
    [0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],
    [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]
])
cube_edges = [
    [0, 1], [1, 2], [2, 3], [3, 0],
    [4, 5], [5, 6], [6, 7], [7, 4],
    [0, 4], [1, 5], [2, 6], [3, 7]
]

def plot_3d_object(vertices, edges, title):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter3D(vertices[:, 0], vertices[:, 1], vertices[:, 2], color='b')

    for edge in edges:
        ax.plot3D([vertices[edge[0], 0], vertices[edge[1], 0]],
                  [vertices[edge[0], 1], vertices[edge[1], 1]],
                  [vertices[edge[0], 2], vertices[edge[1], 2]], color='b')

    ax.set_title(title)

    ax.set_box_aspect([1, 1, 1])

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    ax.grid(True)

    plt.show()

plot_3d_object(cube_vertices, cube_edges, 'Cube')


