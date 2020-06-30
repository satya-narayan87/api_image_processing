import uvicorn
from fastapi import FastAPI

#Intialization of app
app = FastAPI()

#Routes
@app.get('/')
async def index():
    return {"text": "Hello api master"}

@app.get('/items/{name}')
async def get_items(name):
    return {"name": name}

@app.post('/items/{name}')
async def get_items(name):
    return {"name": name}

if __name__ == '__main__':
    uvicorn.run(app,host = "127.0.0.1",port = 8000)