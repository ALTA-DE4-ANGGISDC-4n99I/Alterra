from fastapi import FastAPI
import os

USER_NAME = os.getenv('USER_NAME', 'World')

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": USER_NAME}

# buat running: uvicorn main:app
