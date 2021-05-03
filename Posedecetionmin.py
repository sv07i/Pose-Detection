import cv2
import mediapipe as mp
import time


#mpPose = mp.solutions.pose
#pose = mpPose.Pose()

cap = cv2.VideoCapture(0)
pTime = 0
#cTime = 0
while True:
    success, img = cap.read()
    #imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #results = pose.process(imgRGB)


    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    cv2.putText(img,  str(int(fps)), (70, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)
    #cv2.putText(img, f'FPS: {int(fps)}, (40, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0,0 ), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

