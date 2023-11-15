# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 06:55:38 2023

@author: herna
"""

from fastapi import FastAPI

app = FastAPI(title="API de Hernandes",                         #Cria uma instância do objeto API
              openapi_tags=[                                    # openapi_tags recebe uma lista de dicionários
                  {"name": "Health",
                      "description":"Get API Health"},
                  {"name": "Prediction",
                      "description":"Model Prediction"}])

def load_model():
    #configureMLFLOW
    return 0

@app.get(path="/",                                              #@ é um decorator que envelopa a função, path é a rota e a barra significa raiz
         tags=["Health"])                                       #inclui o método get no tag Health definido na criação da API      
def api_health():
    return {"status":"healthy"}

@app.post(path="/predict",
          tags=["Prediction"])
def predict():
    return {"prediction": 0}
