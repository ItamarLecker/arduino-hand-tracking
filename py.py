import cv2
import mediapipe as mp
import time

from mediapipe.python.solutions.hands_connections import HAND_CONNECTIONS

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

PFT=0

font = cv2.FONT_HERSHEY_SIMPLEX


def culc(px):
    deg = (px - w//2)//2
    print("turn deg = ", deg)


while True:
    success, img = cap.read()
    global h
    global w
    (h, w) = img.shape[:2]
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):

                hh, ww, c = img.shape
                cy = int(lm.y*hh)
                cx = int(lm.x*ww)
                if id == 0:
                    px = cx
                    culc(px)
                if id == 4:
                    (tx, ty) = (cx, cy)
                if id == 8:
                    (ix, iy) = (cx, cy)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
            ln = cv2.line(img, (tx, ty), (ix, iy),
                          (0, 255, 0), thickness=3, lineType=8)
            lineL = int(cv2.norm((tx, ty), (ix, iy)))
            print("speed = ", lineL)

    NFT = time.time()
    fps = 1/(NFT-PFT)
    PFT = NFT

    fps = int(fps)
    fps = str(fps)

    cv2.putText(img, fps, (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)

    src = cv2.circle(img, (w//2, h//2), 7, (0, 0, 255), -1)
    cv2.imshow("img", img)
    cv2.waitKey(1)
