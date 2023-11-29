'''
Unit Electronics 2023
       (o_
(o_    //\
(/)_   V_/_ 

file: write_json.py
'''
import ujson as json

state = False 
jsonData = {"stateKey": state} 

try:
    with open('data.json', 'w') as f:
        json.dump(jsonData, f)
except:
        print("Error!!  No puede almacenar datos")