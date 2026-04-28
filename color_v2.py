import cv2
import numpy as np

# Tus valores calibrados
COLORES = {
    "Rojo":     ([153, 140,  56], [179, 255, 255]),
    "Rojo2":    ([0,   140,  56], [10,  255, 255]),  # segundo rango del rojo
    "Azul":     ([46,  170,   0], [179, 255, 255]),
    "Amarillo": ([0,    54,  67], [64,  255, 231]),
}

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    color_detectado = None
    area_maxima = 0
    cx = cy = cr = 0

    for nombre, (lower, upper) in COLORES.items():
        mask = cv2.inRange(hsv, np.array(lower), np.array(upper))
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)

        contours, _ = cv2.findContours(
            mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )

        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 800 and area > area_maxima:
                area_maxima = area
                ((x, y), radius) = cv2.minEnclosingCircle(cnt)
                if radius > 10:
                    
                    color_detectado = nombre.replace("2", "")
                    cx, cy, cr = int(x), int(y), int(radius)

    if color_detectado:
        cv2.circle(frame, (cx, cy), cr, (0, 255, 0), 3)
        cv2.putText(frame, color_detectado, (cx - 40, cy - cr - 15),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
        print(f"Detectado: {color_detectado}")
    else:
        cv2.putText(frame, "Sin deteccion", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

    cv2.imshow("Detector de Bolas", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
