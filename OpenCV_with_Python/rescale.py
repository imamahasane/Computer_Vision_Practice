import cv2 as cv

img = cv.imread("/Users/imamahasan/python/OpenCV_with_Python/Photos/cat_large.jpg")
cv.imshow("Cat", img)

def rescaleFrame(frame, scale = 0.75):
    # Images, Videos, Live Videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimension = (width, height)

    return cv.resize(frame, dimension, interpolation = cv.INTER_AREA)

def changeRes(width, height):
    # Live Videos
    cap.set(3, width)
    cap.set(4, height)

# Resize Image
resize_image = rescaleFrame(img) 
cv.imshow("Image", resize_image)

# Reading Video
cap = cv.VideoCapture("/Users/imamahasan/python/OpenCV_with_Python/Videos/dog.mp4")

while True:
    isTrue, frame = cap.read()
    frame_resized = rescaleFrame(frame, scale = .2)

    cv.imshow("Video", frame)
    cv.imshow("Video Resize", frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

cap.release()
cv.destroyAllWindows()