from picamera2 import Picamera2
import cv2
import numpy as np

picam2 = Picamera2()
picam2.start()

while True:
    frame = picam2.capture_array()
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    
    # aquí va tu código de detección de colores
    cv2.imshow("Camara", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

picam2.stop()



