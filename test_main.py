from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_capture_employee():
    response = client.post("/employees", json = {
        "emp_number":"TS00554",
        "phone_number":"0794986977",
        "first_name":"Pedro",
        "last_name":"Ferreira"
    })
    assert response.status_code == 200

def test_get_employees():
    response = client.get("/employees")
    assert response.status_code == 200

def test_capture_leave():
    response = client.post("/leave", json = {
        "employee_pk":"TS00554",
        "start_date":"2022-08-10",
        "end_date":"2022-08-10",
        "days_of_leave":"1"
    })
    assert response.status_code == 200


    #valid employee no
        response = client.post("/leave", json = {
        "employee_pk":"000000",
        "start_date":"2022-08-10",
        "end_date":"2022-08-11",
        "days_of_leave":"1"
    })
    assert response.status_code == 422
    
    #start_date check
    response = client.post("/leave", json = {
        "employee_pk":"TS00554",
        "start_date":"2022-08-11",
        "end_date":"2022-08-10",
        "days_of_leave":"1"
    })
    assert response.status_code == 422
