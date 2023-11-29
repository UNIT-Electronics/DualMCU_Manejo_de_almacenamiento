# -*- coding: utf-8 -*-
"""
Unit Electronics 2023
       (o_
(o_    //\
(/)_   V_/_ 

Author: Cesar
Compilador:
MicroPython v1.21.0 on 2023-10-05; Generic ESP32 module with ESP32
MicroPython v1.20.0-219-g47dc7d013 on 2023-06-15; Raspberry Pi Pico W with RP2040

Date: 06/11/2023
Version: 1.0
Description:
    This Python script is intended to manage and store data in JSON format while also creating backups of different states.
    It specifically configures the data format using the "stateKey" parameter.
    The primary purpose of this code is to increment a counter from 0 to 100 continuously, ensuring that the data is saved periodically during the loop.
"""
import ujson as json
import time

def cargar_ultimo_valor():
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
            return data.get("stateKey", 0)
    except:
        print("Error! No se pudo cargar el último valor.")
        return 0

def guardar_ultimo_valor(valor):
    jsonData = {"stateKey": valor}
    try:
        with open('data.json', 'w') as f:
            json.dump(jsonData, f)
    except:
        print("Error! No se pudo guardar el último valor.") 

while True:
    valor_actual = cargar_ultimo_valor()
    if valor_actual == 100:
            valor_actual=0

    for i in range(valor_actual, 101):
        print(f"Valor actual: {i}")
        valor_actual = i
        guardar_ultimo_valor(valor_actual)
        
        time.sleep(1)  

    print("Contador completado. Reinicio de contador en 'savedata.json'.")