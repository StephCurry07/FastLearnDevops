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

@app.get("/stress")
def stress(seconds: int = 5):
    start = time.time()
    x = 0
    # CPU-intensive loop
    while time.time() - start < seconds:
        x += 1
    return {"status": "stressed", "iterations": x}
