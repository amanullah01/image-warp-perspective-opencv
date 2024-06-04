import cv2

input_image = cv2.imread('./images/cards2.jpg')
image = cv2.resize(input_image, (0, 0), None, 0.6, 0.6)

cv2.imshow('image', image)
cv2.waitKey(0)
