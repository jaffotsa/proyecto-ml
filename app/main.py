from fastapi import FastAPI
from pydantic import BaseModel
from app.model.model import predict_pipeline
from app.model.model import __version__ as model_version

# Vamos a inicializar la aplicacion

app = FastAPI()


# Una class es como una función pero estas sirven para procesar datos y segmentar un algoritmo


class TextIn(BaseModel):
    text:str # me va a agarrar lo que yo tenga como texto a clasificar y lo va a exportar como STRING

class PredictionOut(BaseModel):
    language:str # es la predicción que arroja el modelo, la convierte a string y me lo ofrece para visualizar

### ordenes de ejecucion de aplicaciones:
##### @app.get - checar salud de la app (version)
##### @app.post - (para hacer correr la aplicación)

@app.get("/")
def home():
    return {'health_check':'OK', "model_version": model_version}

@app.post("/predict", response_model = PredictionOut)
def predict(payload: TextIn) #payload es para regresar respuesta dinámica
    language = predict_pipeline(payload.text)
    return{"language":language}