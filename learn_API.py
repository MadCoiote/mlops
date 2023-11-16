# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 06:55:38 2023

@author: herna
"""

from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np


class input_data(BaseModel):
    feature0 = float
    feature1 = float
    feature2 = float
    feature3 = float

app = FastAPI(title="API de Hernandes",                         #Cria uma instância do objeto API
              openapi_tags=[                                    # openapi_tags recebe uma lista de dicionários
                  {"name": "Health",
                      "description":"Get API Health"},
                  {"name": "Prediction",
                      "description":"Model Prediction"}])

def load_model():
    #configureMLFLOW
    return 0

@app.on_event(event_type="startup")
def start_event():
    global model
    loaded_model = load_model()


@app.get(path="/",                                              #@ é um decorator que envelopa a função, path é a rota e a barra significa raiz
         tags=["Health"])                                       #inclui o método get no tag Health definido na criação da API      
def api_health():
    return {"status":"healthy"}


@app.post(path="/predict",
          tags=["Prediction"])
def predict(request: input_data):
    global loaded_model
    pred_data = np.array([request.feature0,
                          request.feature1,
                          request.feature2,
                          request.feature3])
    prediction = loaded_model.predict(pred_data)
    return {"prediction": str(np.argmax(prediction[0]))}
    
