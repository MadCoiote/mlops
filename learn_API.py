# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 06:55:38 2023

@author: herna
"""

from fastapi import FastAPI

app = FastAPI()
@app.get(path="/")

def home():
    return {"status":"healthy"}