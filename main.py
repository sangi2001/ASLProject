import cv2
import mediapipe as mp

my_list = []

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

finger_tips = [8, 12, 16, 20]
thumb_tip = 4

while True:
    ret, img = cap.read()
    img = cv2.flip(img, 1)
    h, w, c = img.shape
    results = hands.process(img)
    if results.multi_hand_landmarks:
        for hand_landmark in results.multi_hand_landmarks:
            lm_list = []
            for id, lm in enumerate(hand_landmark.landmark):
                lm_list.append(lm)
            finger_fold_status = []
            for tip in finger_tips:
                x, y = int(lm_list[tip].x * w), int(lm_list[tip].y * h)
                # print(id, ":", x, y)
                # cv2.circle(img, (x, y), 15, (255, 0, 0), cv2.FILLED)

                if lm_list[tip].x < lm_list[tip - 2].x:
                    # cv2.circle(img, (x, y), 15, (0, 255, 0), cv2.FILLED)
                    finger_fold_status.append(True)
                else:
                    finger_fold_status.append(False)

            print(finger_fold_status)

            x, y = int(lm_list[8].x * w), int(lm_list[8].y * h)
            print(x, y)
            # fuck off
            if lm_list[3].x < lm_list[4].x and lm_list[8].y > lm_list[6].y and lm_list[12].y < lm_list[10].y and \
                    lm_list[16].y > lm_list[14].y and lm_list[20].y > lm_list[18].y:
                cv2.putText(img, "fuck off !!!", (200, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

            # D
            if lm_list[2].x > lm_list[3].x and lm_list[8].y < lm_list[6].y and lm_list[12].y > lm_list[10].y and \
                    lm_list[16].y > lm_list[14].y and lm_list[20].y > lm_list[18].y:
                cv2.putText(img, "D", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                my_list.append("D")

            # N
            if lm_list[4].x > lm_list[10].x and lm_list[8].y > lm_list[6].y and lm_list[12].y > lm_list[10].y and \
                    lm_list[16].y > lm_list[14].y and lm_list[20].y > lm_list[18].y:
                cv2.putText(img, "N", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                my_list.append("N")

            # V
            if lm_list[3].x > lm_list[4].x and lm_list[8].y < lm_list[6].y and lm_list[12].y < lm_list[10].y and \
                    lm_list[16].y > lm_list[14].y and lm_list[20].y > lm_list[18].y:
                cv2.putText(img, "V", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                my_list.append("V")

            # W
            if lm_list[19].x > lm_list[4].x and lm_list[8].y < lm_list[6].y and lm_list[12].y < lm_list[10].y and \
                    lm_list[16].y < lm_list[14].y and lm_list[19].y > lm_list[17].y:
                cv2.putText(img, "W", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                my_list.append("W")

            # C
            if lm_list[4].x > lm_list[3].x and lm_list[8].y > lm_list[7].y and lm_list[12].y > lm_list[11].y and \
                    lm_list[16].y > lm_list[15].y and lm_list[20].y > lm_list[19].y:
                cv2.putText(img, "C", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                my_list.append("C")

            # F
            if lm_list[4].x > lm_list[2].x and lm_list[8].y > lm_list[6].y and lm_list[12].y < lm_list[10].y and \
                    lm_list[16].y < lm_list[14].y and lm_list[20].y > lm_list[18].y:
                cv2.putText(img, "F", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                my_list.append("F")

            # Y
            if lm_list[3].x > lm_list[4].x and lm_list[8].y > lm_list[7].y and lm_list[12].y > lm_list[11].y and \
                    lm_list[16].y > lm_list[14].y and lm_list[20].y < lm_list[19].y:
                cv2.putText(img, "Y", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                my_list.append("Y")

            # S
            if lm_list[4].x > lm_list[10].x and lm_list[8].y > lm_list[6].y and lm_list[12].y > lm_list[10].y and \
                    lm_list[16].y > lm_list[14].y and lm_list[20].y > lm_list[18].y:
                cv2.putText(img, "S", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                my_list.append("S")

            # X
            if lm_list[4].x > lm_list[3].x and lm_list[8].y < lm_list[7].y and lm_list[12].y > lm_list[10].y and \
                    lm_list[16].y > lm_list[14].y and lm_list[20].y > lm_list[18].y:
                cv2.putText(img, "X", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                my_list.append("X")

            # K
            if lm_list[4].x > lm_list[10].x and lm_list[8].y < lm_list[6].y and lm_list[12].y < lm_list[10].y and \
                    lm_list[16].y > lm_list[14].y and lm_list[20].y > lm_list[18].y:
                cv2.putText(img, "K", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                my_list.append("K")

            # A
            if lm_list[3].x > lm_list[4].x and lm_list[8].y > lm_list[6].y and lm_list[12].y > lm_list[10].y and \
                    lm_list[16].y > lm_list[14].y and lm_list[20].y > lm_list[18].y:
                cv2.putText(img, "A", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                my_list.append("A")

            # B
            if lm_list[4].x > lm_list[3].x and lm_list[8].y < lm_list[6].y and lm_list[12].y < lm_list[10].y and \
                    lm_list[16].y < lm_list[14].y and lm_list[20].y < lm_list[18].y:
                cv2.putText(img, "B", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                my_list.append("B")

            # E
            if lm_list[4].x > lm_list[2].x and lm_list[8].y > lm_list[6].y and lm_list[12].y > lm_list[10].y and \
                    lm_list[16].y > lm_list[14].y and lm_list[20].y > lm_list[18].y:
                cv2.putText(img, "E", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                my_list.append("E")

            # H
            if lm_list[4].x > lm_list[3].x and lm_list[7].y > lm_list[8].y and lm_list[11].y > lm_list[12].y and \
                    lm_list[15].y > lm_list[16].y and lm_list[19].y > lm_list[20].y:
                cv2.putText(img, "H", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                my_list.append("H")

            # G
            if lm_list[4].x > lm_list[3].x and lm_list[7].y > lm_list[8].y and lm_list[11].y < lm_list[12].y and \
                    lm_list[15].y > lm_list[16].y and lm_list[19].y > lm_list[20].y:
                cv2.putText(img, "G", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                my_list.append("G")

            # I
            if lm_list[3].x < lm_list[4].x and lm_list[8].y > lm_list[6].y and lm_list[12].y > lm_list[10].y and \
                    lm_list[16].y > lm_list[14].y and lm_list[20].y < lm_list[18].y:
                cv2.putText(img, "I", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                my_list.append("I")

            # L
            if lm_list[3].x > lm_list[4].x and lm_list[8].y < lm_list[6].y and lm_list[12].y > lm_list[10].y and \
                    lm_list[16].y > lm_list[14].y and lm_list[20].y > lm_list[18].y:
                cv2.putText(img, "L", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                my_list.append("L")

            # M
            if lm_list[4].x > lm_list[14].x and lm_list[8].y > lm_list[6].y and lm_list[12].y > lm_list[10].y and \
                    lm_list[16].y > lm_list[14].y and lm_list[20].y > lm_list[18].y:
                cv2.putText(img, "M", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                my_list.append("M")

            # S
            if lm_list[3].x > lm_list[4].x and lm_list[8].y > lm_list[6].y and lm_list[12].y > lm_list[10].y and \
                    lm_list[16].y > lm_list[14].y and lm_list[20].y > lm_list[18].y:
                cv2.putText(img, "S", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                my_list.append("S")

            # T
            if lm_list[3].x < lm_list[4].x and lm_list[8].y < lm_list[6].y and lm_list[12].y > lm_list[10].y and \
                    lm_list[16].y > lm_list[14].y and lm_list[20].y > lm_list[18].y:
                cv2.putText(img, "T", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                my_list.append("T")

            # R
            if lm_list[3].x > lm_list[4].x and lm_list[8].y > lm_list[12].y and lm_list[12].y < lm_list[10].y and \
                    lm_list[16].y > lm_list[14].y and lm_list[20].y > lm_list[18].y:
                cv2.putText(img, "R", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                my_list.append("R")

            # U
            if lm_list[3].x > lm_list[4].x and lm_list[11].y < lm_list[7].y and lm_list[12].y < lm_list[10].y and \
                    lm_list[16].y > lm_list[14].y and lm_list[20].y > lm_list[18].y:
                cv2.putText(img, "U", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                my_list.append("U")



            mp_draw.draw_landmarks(img, hand_landmark,
                                   mp_hands.HAND_CONNECTIONS,
                                   mp_draw.DrawingSpec((0, 0, 255), 6, 3),
                                   mp_draw.DrawingSpec((0, 255, 0), 4, 2)
                                   )
        my_sentense = ''.join(my_list)
        # cv2.putText(img, my_sentense, (200, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 3)
        cv2.imshow("SIGN LANGUAGE DETECTION - SAMEER EDLABADKAR", img)
        cv2.waitKey(1)