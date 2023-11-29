
'''
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
    It specifically configures the data format using the "estadoLED" parameter.
    The primary purpose of this code is to turn on and off an LED using a button, ensuring that the data is saved periodically during the loop.
'''
import ujson as json
import time
from machine import Pin

def cargar_estado_led():
    try:
        with open('statusLED.json', 'r') as f:
            data = json.load(f)
            return data.get("estadoLED", False)  
    except:
        return False

def guardar_estado_led(estado):
    datos_json = {"estadoLED": estado} 
    try:
        with open('statusLED.json', 'w') as f:
            json.dump(datos_json, f)
    except:
        print("No se pudo guardar la variable de estado del LED.")

boton = Pin(16, Pin.IN, Pin.PULL_UP)
led = Pin(17, Pin.OUT)

debounce_time = 0
estado_led = cargar_estado_led()  
led.value(estado_led)

while True:
    if boton.value() == 0 and time.ticks_ms() - debounce_time > 300:
        debounce_time = time.ticks_ms()
        estado_led = not estado_led
        led.value(estado_led)
        guardar_estado_led(estado_led)  
    time.sleep(0.3)
