import cv2

video = cv2.VideoCapture(r"C:\Users\91638\Downloads\The Breathtaking Beauty of Nature _ HD.mp4")
while True:
    status, frame = video.read()
    # print(status, frame)
    if not status:
        break
    cv2.imshow("video frame", frame)
    if cv2.waitKey(1) == 27:
        break
video.release()
cv2.destroyAllWindows()