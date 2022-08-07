from fastapi import FastAPI
from modules.database import Employee
from modules.database import LeaveApplication

app = FastAPI()

dbLeave = LeaveApplication()
dbEmployee = Employee()


@app.get("/")
async def read_root():

    return {"message": "Hello World"}


@app.post("/leave")
async def capture_leave():

    return {"message": "Hello World"}
