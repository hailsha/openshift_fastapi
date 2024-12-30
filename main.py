from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
def index():
    return {'data': 'Hello FastAPI!'}

@app.get('/message')
def index():
    return {'data': 'FastAPI is great!'}
