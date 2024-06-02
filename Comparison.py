import cv2
import numpy as np
import matplotlib.pyplot as plt

def plot_objects_cv(objects, titles):
    fig, axes = plt.subplots(1, len(objects), figsize=(10, 5))
    if len(objects) == 1:
        axes = [axes]

    for ax, obj, title in zip(axes, objects, titles):
        ax.plot(obj[:, 0], obj[:, 1], marker='o')
        ax.set_title(title)
        ax.set_aspect('equal')
        ax.grid(True)

    plt.show()


batman = np.array([
    [0, 0], [1, 0.2], [0.4, 1], [0.5, 0.4], [0, 0.8], [-0.5, 0.4], [-0.4, 1], [-1, 0.2], [0, 0]])


def rotate_object_cv(obj, angle):
    center = (np.mean(obj[:, 0]), np.mean(obj[:, 1]))
    rotation_matrix = cv2.getRotationMatrix2D(center, angle * 180 / np.pi, 1)
    rotated_obj = cv2.transform(obj.reshape((-1, 1, 2)), rotation_matrix).reshape((-1, 2))
    return rotated_obj

rotated_batman_cv = rotate_object_cv(batman, np.pi / 2)
plot_objects_cv([rotated_batman_cv], ["Rotated Batman (OpenCV)"])

def scale_object_cv(obj, scale_factor):
    center = (np.mean(obj[:, 0]), np.mean(obj[:, 1]))
    scaling_matrix = np.array([
        [scale_factor, 0],
        [0, scale_factor]
    ])
    scaled_obj = cv2.transform(obj.reshape((-1, 1, 2)), scaling_matrix).reshape((-1, 2))
    return scaled_obj

scaled_batman_cv = scale_object_cv(batman, 2)
plot_objects_cv([scaled_batman_cv], ["Scaled Batman (OpenCV)"])

def reflect_object_cv(obj, axis):
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
    reflected_obj = cv2.transform(obj.reshape((-1, 1, 2)), reflection_matrix).reshape((-1, 2))
    return reflected_obj

reflected_batman_cv = reflect_object_cv(batman, 'x')
plot_objects_cv([reflected_batman_cv], ["Reflected Batman (OpenCV)"])

def change_object_cv(obj, axis, factor):
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
    changed_obj = cv2.transform(obj.reshape((-1, 1, 2)), changed_matrix).reshape((-1, 2))
    return changed_obj

changed_batman_cv = change_object_cv(batman, 'y', 1.5)
plot_objects_cv([changed_batman_cv], ["Changed Batman (OpenCV)"])

def transform_object_cv(obj, transformation_matrix):
    transformed_obj = cv2.transform(obj.reshape((-1, 1, 2)), transformation_matrix).reshape((-1, 2))
    return transformed_obj

transformation_matrix2_cv = np.array([
    [1.5, 0],
    [0, 2]
])

transformed_batman_cv = transform_object_cv(batman, transformation_matrix2_cv)
plot_objects_cv([transformed_batman_cv], ["Transformed Batman (OpenCV)"])
