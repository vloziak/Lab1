import cv2
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

star = np.array([
    [0, 0.25], [1, 2.25], [2, 0.25], [0, 1.5], [2, 1.5], [0, 0.25]
])
batman = np.array([
    [0, 0], [1, 0.2], [0.4, 1], [0.5, 0.4], [0, 0.8], [-0.5, 0.4], [-0.4, 1], [-1, 0.2], [0, 0]])
def plot_objects(objects, titles):
    fig, axes = plt.subplots(1, len(objects), figsize=(10, 5))
    if len(objects) == 1:
        axes = [axes]

    for ax, obj, title in zip(axes, objects, titles):
        ax.plot(obj[:, 0], obj[:, 1], marker='o')
        ax.set_title(title)
        ax.set_aspect('equal')
        ax.grid(True)

    plt.show()

plot_objects([star, batman], ['Star', 'Batman'])

def rotate_object(obj, angle):
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    rotated_obj = np.dot(obj, rotation_matrix)
    print("Rotation Matrix:")
    print(rotation_matrix)
    return rotated_obj

rotated_star = rotate_object(star, np.pi / 2)
rotated_batman = rotate_object(batman, np.pi / 2)
plot_objects([rotated_star, rotated_batman], ["Rotated Star", "Rotated Batman"])

def scale_object(obj, scale_factor):
    scaling_matrix = np.array([
        [scale_factor, 0],
        [0, scale_factor]
    ])
    scaled_obj = np.dot(obj, scaling_matrix)
    print("Scaling Matrix:")
    print(scaling_matrix)
    return scaled_obj


scaled_star = scale_object(star, 2)
scaled_batman = scale_object(batman, 2)
plot_objects([scaled_star, scaled_batman], ["Scaled Star", "Scaled Batman"])

def reflect_object(obj, axis):
    if axis == 'x':
        reflection_matrix = np.array([
            [1, 0],
            [0, -1]
        ])
    elif axis == 'y':
        reflection_matrix = np.array([
            [-1, 0],
            [0, 1]
        ])
    reflected_obj = np.dot(obj, reflection_matrix)
    print("Reflected Matrix: ")
    print(reflection_matrix)
    return reflected_obj

reflected_star = reflect_object(star, 'y')
reflected_batman = reflect_object(batman, 'x')
plot_objects([reflected_star,reflected_batman], ["Reflected Star", "Reflected Batman"])

def change_object(obj, axis, factor):
    if axis == 'x':
        changed_matrix = np.array([
            [1, factor],
            [0, 1]
        ])
    elif axis == 'y':
        changed_matrix = np.array([
            [1, 0],
            [factor, 1]
        ])
    changed_obj = np.dot(obj, changed_matrix)
    print("Changed Matrix")
    print(changed_matrix)
    return changed_obj

changed_star = change_object(star,'x', 1.5)
changed_batman = change_object(batman,'y', 1.5)
plot_objects([changed_star,changed_batman], ["Changed Star", "Changed Batman"])

def transform_object(obj, transformation_matrix):
    transformed_obj = np.dot(obj, transformation_matrix)
    print("Transformation Matrix")
    print(transformation_matrix)
    return transformed_obj

transformation_matrix1 = np.array([
    [2, 0],
    [0, 0.5]
])
transformation_matrix2 = np.array([
    [1.5, 0],
    [0, 2]
])

transformed_star = transform_object(star,transformation_matrix1)
transformed_batman = transform_object(batman,transformation_matrix2)
plot_objects([transformed_star,transformed_batman],["Transformed Star", "Transformed Batman"])