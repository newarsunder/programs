import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width, _ = frame.shape

    cx = int(width / 2)
    cy = int(height / 2)
    pixel_centre = hsv_frame[cy, cx]
    p = frame[cy, cx]
    B = int(p[0])
    G = int(p[1])
    R = int(p[2])
    color = ""
    hue_pixel = pixel_centre[0]
    s, v = pixel_centre[1], pixel_centre[2]
    # print(s,v)

    if hue_pixel <= 4:
        color = "RED"
    elif 5 <= hue_pixel <= 20:
        color = "ORANGE"
    elif 21 <= hue_pixel <= 39:
        color = "YELLOW"
    elif 40 <= hue_pixel <= 82:
        color = "GREEN"
    elif 83 <= hue_pixel <= 91:
        color = "CYAN"
    elif 92 <= hue_pixel <= 127:
        color = "BLUE"
    elif 128 <= hue_pixel <= 142:
        color = "PURPLE"
    elif 143 <= hue_pixel <= 166:
        color = "PINK"
    elif 167 <= hue_pixel <= 179:
        color = "RED"

    if s<90:
        if v<70:
            color = "BLACK"
        elif v>233:
            color = "WHITE"
    cv2.putText(frame, color, (10, 50), 0, 1, (B, G, R), 2)
    cv2.circle(frame, (cx, cy), 5, (255, 0, 0), 3)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
