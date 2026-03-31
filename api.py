

from typing import Union
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pathlib import Path
import os

app = FastAPI()


@app.get("/prueba")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/camera")
def capture_image():
    os.system('python camera-service.py')
    image_path = Path("C:/Users/sersatr/Repositorios/vision-yolo-system/dataset/capturas/result.jpg")
    if not image_path.is_file():
        return {"error": "Image not found on the server"}
    return FileResponse(image_path)


@app.get("/inference")
def run_inference():   
    os.system('python inference-service.py')
    image_path = Path("C:/Users/sersatr/Repositorios/vision-yolo-system/runs/detect/predict8/result.jpg")
    if not image_path.is_file():
        return {"error": "Image not found on the server"}
    return FileResponse(image_path)

