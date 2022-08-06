from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Hello World"}


@app.post("/leave")
async def capture_leave():
    return {"message": "Hello World"}
