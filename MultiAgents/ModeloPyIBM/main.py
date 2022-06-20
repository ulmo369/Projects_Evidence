""" Importamos el modelo del archivo en que lo definimos. """
from streetModel import StreetModel
from streetModel import get_grid

""" Importamos los siguientes paquetes para el mejor manejo de valores
    numéricos."""
import numpy as np
import pandas as pd
import random

""" Definimos otros paquetes que vamos a usar para medir el tiempo de
    ejecución de nuestro algoritmo. """
import time
import datetime

""" Para coneccion con IBM """
from flask import Flask, render_template, request, jsonify
import json, logging, os, atexit

# INFORMACION DE LA WAREHOUSE:
WIDTH = 10
HEIGHT = 10
NUM_CARS = 20

#Tiempo de ejecución
"""
TIME = 0.01
moves = 0
MAX_GENERATIONS = 60
ACTUAL_GENERATION = 0
"""

model = StreetModel(WIDTH, HEIGHT, NUM_CARS)

def updatePositions():
    global model
    global ACTUAL
    #ACTUAL = 0
    positions = []
    model.step(NUM_CARS)
    matrix = np.array(get_grid(model))
    print(matrix)
    for x in range(WIDTH):
        for z in range(HEIGHT):
            if (matrix[x, z] != 0):
                pos = [x, z, 0, matrix[x, z]]
                positions.append(pos)
                print(positions)
    #ACTUAL += 1
    return positions

def positionsToJSON(ps):
    posDICT = []
    for p in ps:
        pos = {
            "x" : p[0],
            "z" : p[1],
            "y" : p[2],
            "val" : p[3]
        }
        posDICT.append(pos)
        print(json.dumps(posDICT))
    return json.dumps(posDICT)


app = Flask(__name__, static_url_path='')

# On IBM Cloud Cloud Foundry, get the port number from the environment variable PORT
# When running this app on the local machine, default the port to 8000
port = int(os.getenv('PORT', 8000))

@app.route('/', methods=['POST'])
def root():
    positions = updatePositions()
    #print(positions)
    resp = "{\"data\":" + positionsToJSON(positions) + "}"
    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)