from fastapi import FastAPI
from modules.database import Employees
from modules.database import LeaveApplications
from modules.models import Employee
from modules.models import Leave

app = FastAPI()
dbLeave = LeaveApplications()
dbEmployee = Employees()

Employee


@app.get("/")
async def read_root():

    return {"message": "Hello World"}


@app.post("/leave")
async def capture_leave(leave: Leave):

    return {"message": "Hello World", "leave": leave}
