from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def Home():
    return {"message": "Hello World from twitter app"}