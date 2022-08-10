from fastapi import FastAPI
from modules.database import Employees
from modules.database import LeaveApplications
from modules.models import Leave

app = FastAPI(
    docs_url="/api/v1/docs",
    redoc_url="/api/v1/docs",
    title="Leave Application API",
    description="Demo of basic Rest API for employees to log their leave for Tangent Solutions",
    version="1.0",
    openapi_url="/api/v1/openapi.json"
)
dbLeave = LeaveApplications()
dbEmployee = Employees()


@app.get("/")
async def read_root():
    return {"message": "Hello World"}


@app.post("/leave")
async def capture_leave(leave: Leave):
    dbLeave.insert(
        (
            leave.employee_pk,
            leave.start_date,
            leave.end_date,
            leave.days_of_leave,
            leave.status,
        )
    )
    return leave
