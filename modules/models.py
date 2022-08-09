from datetime import date

from dateutil.parser import parse
from pydantic import BaseModel
from pydantic import root_validator


class Employee(BaseModel):
    emp_number: str
    phone_number: str
    first_name: str
    last_name: str


class Leave(BaseModel):
    employee_pk: str
    start_date: date
    end_date: date
    days_of_leave: int
    status: str = "New"

    @root_validator(pre=True)
    def validate_is_before_end_date(cls, leave):
        if parse(leave["start_date"]) > parse(leave["end_date"]):
            raise ValueError("start date must be before end date")
        return leave
