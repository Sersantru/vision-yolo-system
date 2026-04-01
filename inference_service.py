from ultralytics import YOLO
import cv2
from pathlib import Path

RESULT_PATH = Path("C:/Users/sersatr/Repositorios/vision-yolo-system/dataset/inferencias/result.jpg")
model = 'C:/Users/sersatr/Repositorios/vision-yolo-system/train2/weights/best.pt'
modelo_entrenado = YOLO(model)
img = "C:/Users/sersatr/Repositorios/vision-yolo-system/dataset/capturas/result.jpg"

def inference():

    resultados = modelo_entrenado.predict(img)
    inferencia = resultados[0].plot()
    cv2.imwrite(str(RESULT_PATH), inferencia)

    return RESULT_PATH

