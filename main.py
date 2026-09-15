from fastapi import FastAPI
import json

app= FastAPI()

def load_data():
    with open('patients.json','r') as f:
        data = json.load(f)

    return data



@app.get("/")
def hello():
    return {'message':'Hello world'}

@app.get('/about')
def message():
    return {'message':'A fully functional api to manae the patients records'}

@app.get('/view')
def view():
    data = load_data()
    return data