from fastapi import FastAPI

app= FastAPI()

@app.get("/")
def hello():
    return {'message':'Hello world'}

@app.get('/about')
def message():
    return {'message':'Heyy this is deepak i am learning fast api'}