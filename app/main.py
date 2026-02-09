from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return "Hello"

@app.get("/health")
def check_health():
    return {"status": "ok"}

@app.get("/infer")
def infer():
    return "Inferring this API"


