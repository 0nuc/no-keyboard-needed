import cv2
import pyautogui
import mediapipe as mp
import os

#Capture / lis et affiche le flux
cap = cv2.VideoCapture(0)



# Vérifier si la webcam s'ouvre



mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False , max_num_hands=1,min_detection_confidence=0.5,min_tracking_confidence=0.5)

mp_drawing = mp.solutions.drawing_utils

while True:
    ret , frame = cap.read()
    if not ret:
        break
    
    image_rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    results = hands.process(image_rgb)
    

    # Dessine les ligne sur la main
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame,hand_landmarks,mp_hands.HAND_CONNECTIONS)
    
        index_finger_y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
        thumb_y = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y

        if index_finger_y > thumb_y:
            hand_gesture = 'down'
        else:
            hand_gesture='other'

        if hand_gesture == 'down':
            os.system('shutdown -s')
    cv2.imshow('Cam',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
