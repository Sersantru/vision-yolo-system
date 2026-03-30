from ultralytics import YOLO

modelo_entrenado = YOLO('C:/Users/sersatr/Repositorios/vision-yolo-system/train2/weights/best.pt')
resultados = modelo_entrenado.predict('C:/Users/sersatr/Repositorios/vision-yolo-system/dataset/capturas/result.jpg', save=True)