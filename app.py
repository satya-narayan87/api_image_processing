import uvicorn
from fastapi import FastAPI

#Intialization of app
app = FastAPI()

#Routes
@app.get('/')
async def index():
    return {"text": "Hello api master"}

if __name__ == '__main__':
    uvicorn.run(app,host = "127.0.0.1",port = 8000)