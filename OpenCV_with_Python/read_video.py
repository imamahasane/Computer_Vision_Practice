import cv2 as cv

cap = cv.VideoCapture("/Users/imamahasan/python/OpenCV_with_Python/Videos/dog.mp4")

while True:
    isTrue, frame = cap.read()
    cv.imshow("Video", frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

cap.release()
cv.destroyAllWindows()