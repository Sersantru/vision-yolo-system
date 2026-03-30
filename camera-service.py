import cv2
import IPython.display as display
from PIL import Image
import io

def webcam():
    cap = cv2.VideoCapture(0)  # Open the default camera
    ret, frame = cap.read()

    # Resize to speed up processing
    frame = cv2.resize(frame, (640, 480))
    # Convert frame to JPEG format for Jupyter display
    _, buffer = cv2.imencode('.jpg', frame)
    img_data = buffer.tobytes()
    imagen = Image.open(io.BytesIO(img_data))
    return imagen

img = webcam()
img.save("C:/Users/sersatr/Repositorios/vision-yolo-system/dataset/capturas/result.jpg")