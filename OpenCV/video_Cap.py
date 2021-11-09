import cv2

capture = cv2.VideoCapture("/Users/macbookair/Python/OpenCV/video/Sukumar.mp4")

while True:
    nonger, image = capture.read()
    cv2.imshow("Video Fream", image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    