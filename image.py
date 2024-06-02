import numpy as np
import cv2 as cv

img = cv.imread('C:\\Users\\Professional\\Downloads\\Гоша.jpg')
new_width = int(img.shape[1] * 0.75)
new_height = int(img.shape[0] * 0.75)
resized_img = cv.resize(img, (new_width, new_height))
cv.imshow('Gosha', resized_img)
cv.waitKey(0)
cv.destroyAllWindows()

rotated_image = cv.rotate(resized_img, cv.ROTATE_90_CLOCKWISE)
cv.imshow('Rotated Image', rotated_image)
cv.waitKey(0)
cv.destroyAllWindows()


def reflect_image(image, direction):
    if direction == 'y':
        reflected_image = cv.flip(image, 1)
    elif direction == 'x':
        reflected_image = cv.flip(image, 0)
    return reflected_image

reflected_image_y= reflect_image(resized_img, 'y')
cv.imshow('Reflected image y', reflected_image_y)
cv.waitKey(0)
cv.destroyAllWindows()

reflected_image_x = reflect_image(resized_img,'x')
cv.imshow('Reflected image x', reflected_image_x)
cv.waitKey(0)
cv.destroyAllWindows()
