'''
Unit Electronics 2023
       (o_
(o_    //\
(/)_   V_/_ 

file: read_json.py
'''
import ujson as json

try:
    with open('data.json', 'r') as f:
        jsonData = json.load(f)
        state = jsonData.get("stateKey")  

    print("Estado almacenado:", state)
except FileNotFoundError:
    print("El archivo 'data.json' no existe.")
except json.JSONDecodeError:
    print("Error al decodificar el archivo JSON.")
except Exception as e:
    print("Ocurrió un error inesperado:", str(e))