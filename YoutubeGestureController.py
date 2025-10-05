import cv2
import pyautogui
from HandTrackingModule import handDetector
import time

detector = handDetector()
cap = cv2.VideoCapture(0)

# Cooldown time system
cooldown_time = 3
last_action_time = 0

while True:
    success, img = cap.read()
    img = detector.findHands(img)

    fingers = detector.getFingers(img, handNo=0, handType="Right")  # or get label from results
    gesture_text = ""

    current_time = time.time()

    if fingers == [0, 1, 1, 1, 1]:
        gesture_text = "Play"
        if current_time - last_action_time > cooldown_time:
            pyautogui.press("k")
            last_action_time = current_time

    elif fingers == [1, 0, 0, 0, 0]:
        gesture_text = "Pause"
        if current_time - last_action_time > cooldown_time:
            pyautogui.press("k")
            last_action_time = current_time

    elif fingers == [1, 1, 0, 0, 0]:
        gesture_text = "Next Video"
        if current_time - last_action_time > cooldown_time:
            pyautogui.hotkey("shift", "n")
            last_action_time = current_time

    cv2.putText(img, gesture_text, (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    cv2.imshow("Hand Control", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
