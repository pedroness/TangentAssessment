from fastapi import FastAPI
from modules.database import Employees
from modules.database import LeaveApplications
from modules.models import Leave
from modules.models import Employee

app = FastAPI(
    docs_url="/api/v1/docs",
    redoc_url="/api/v1/redocs",
    title="Leave Application API",
    description="Tangent Solutions Interview Assignment, Rest API for employees to log their leave",
    version="1.0",
    openapi_url="/api/v1/openapi.json"
)
dbLeave = LeaveApplications()
dbEmployee = Employees()


@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.get("/employees",  tags=["Employees"])
async def get_employees():
    employees=dbEmployee.read()    
    return employees

@app.post("/employees", tags=["Employees"])
async def capture_employee(employee: Employee):
    dbEmployee.insert(
        (
            employee.emp_number,
            employee.phone_number,
            employee.first_name,
            employee.last_name,
        )
    )
    return employee

@app.post("/leave", tags=["Employee Leave"])
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

@app.get("/leave", tags=["Employee Leave"])
async def get_leave():
    leave=dbLeave.read()    
    return leave