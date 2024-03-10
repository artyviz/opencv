import cv2
import mediapipe as mp
import time

cam = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0


while True:
    success, img = cam.read()

    if not success:
        print("Failed to read frame from camera.")
        break

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
       for handLms in results.multi_hand_landmarks:
           for id , lm in enumerate(handLms.landmark):
               h,w,c = img.shape
               cx,cy = int(lm.x*w),int(lm.y * h)
               print(id,cx,cy)
           mpDraw.draw_landmarks(img , handLms , mpHands.HAND_CONNECTIONS)


    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime


    cv2.putText(img , str(int(fps)), (10,70), cv2.FONT_HERSHEY_TRIPLEX , 3, (230, 230, 250),3)

    cv2.imshow("HAND DETECTION", img)
    cv2.waitKey(1)
