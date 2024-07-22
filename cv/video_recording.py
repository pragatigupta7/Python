#pip install opencv-contrib-python
#pip install mediapipe       #   for AI
import cv2

video = cv2.VideoCapture(r"C:\Users\91638\Downloads\The Breathtaking Beauty of Nature _ HD.mp4")
codec = cv2.VideoWriter_fourcc(*"MP4V")
output = cv2.VideoWriter("output.avi",codec,20.0,(640,480))


while True:
    status, frame = video.read()
    # print(status, frame)
    if not status:
        break
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    output.write(gray)                      #recording
    cv2.imshow("video frame",frame)
    
    if cv2.waitKey(1) == 27:
        break
video.release()
output.release()
cv2.destroyAllWindows()