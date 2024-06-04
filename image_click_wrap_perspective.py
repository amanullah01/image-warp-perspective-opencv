import cv2

input_image = cv2.imread('./images/cards2.jpg')
image = cv2.resize(input_image, (0, 0), None, 0.6, 0.6)

counter = 0


def mouseclick(event, x, y, flags, param):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        counter += 1
        print(f"Mouse click: {counter}")


while True:
    cv2.imshow('image', image)
    cv2.setMouseCallback('image', mouseclick)
    if cv2.waitKey(1) & 0xFF == ord('1'):
        break
