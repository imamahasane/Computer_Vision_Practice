import cv2

cap = cv2.VideoCapture("Resources/AnneMarie.mp4")

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
