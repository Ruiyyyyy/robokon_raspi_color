import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0)

cv2.namedWindow("Calibrador")

# Sliders para ajustar rango HSV
cv2.createTrackbar("H min", "Calibrador", 0, 179, nothing)
cv2.createTrackbar("H max", "Calibrador", 179, 179, nothing)
cv2.createTrackbar("S min", "Calibrador", 0, 255, nothing)
cv2.createTrackbar("S max", "Calibrador", 255, 255, nothing)
cv2.createTrackbar("V min", "Calibrador", 0, 255, nothing)
cv2.createTrackbar("V max", "Calibrador", 255, 255, nothing)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Leer valores de sliders
    h_min = cv2.getTrackbarPos("H min", "Calibrador")
    h_max = cv2.getTrackbarPos("H max", "Calibrador")
    s_min = cv2.getTrackbarPos("S min", "Calibrador")
    s_max = cv2.getTrackbarPos("S max", "Calibrador")
    v_min = cv2.getTrackbarPos("V min", "Calibrador")
    v_max = cv2.getTrackbarPos("V max", "Calibrador")

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    mask = cv2.inRange(hsv, lower, upper)
    resultado = cv2.bitwise_and(frame, frame, mask=mask)

    # Mostrar valores actuales en pantalla
    texto = f"H:{h_min}-{h_max} S:{s_min}-{s_max} V:{v_min}-{v_max}"
    cv2.putText(frame, texto, (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    cv2.imshow("Camara Original", frame)
    cv2.imshow("Calibrador", mask)
    cv2.imshow("Resultado", resultado)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
