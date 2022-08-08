from datetime import date

from pydantic import BaseModel


class Employee(BaseModel):
    emp_number: str
    phone_number: str
    first_name: str
    last_name: str


class Leave(BaseModel):
    employee_pk: str
    start_date: date
    end_date: date
    days_of_leave = int
    status: str = "New"
