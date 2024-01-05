from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def HomePage():
    return {"message:" "Hello World"}