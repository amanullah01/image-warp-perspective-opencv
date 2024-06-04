import cv2
import numpy as np

input_image = cv2.imread('./images/cards2.jpg')
image = cv2.resize(input_image, (0, 0), None, 0.6, 0.6)
circles = np.zeros((4, 2), int)
print("circles", circles)

counter = 0


def mouseclick(event, x, y, flags, param):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        circles[counter] = x, y
        counter += 1
        print(f"Mouse click: {counter}", circles)


while True:
    if counter == 4:
        width, height = 500, 500
        pts1 = np.float32([circles[0], circles[1], circles[2], circles[3]])
        pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        imageOutput = cv2.warpPerspective(image, matrix, (width, height))
        cv2.imshow('imageOutput', imageOutput)

    for x in range(0, 4):
        cv2.circle(image, (circles[x][0], circles[x][1]), 3, (255, 0, 0), -1)

    cv2.imshow('image', image)
    cv2.setMouseCallback('image', mouseclick)
    if cv2.waitKey(1) & 0xFF == ord('1'):
        break
