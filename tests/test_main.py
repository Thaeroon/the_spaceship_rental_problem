from fastapi.testclient import TestClient

from src.the_spaceship_rental_problem.webserver import app

client = TestClient(app)

path = "/spaceship/optimize"


def test_simple():
    input = [
        {"name": "Contract1", "start": 0, "duration": 5, "price": 10},
        {"name": "Contract2", "start": 3, "duration": 7, "price": 14},
        {"name": "Contract3", "start": 5, "duration": 9, "price": 8},
        {"name": "Contract4", "start": 5, "duration": 8, "price": 7},
    ]
    output = {
        "income": 18,
        "path": ["Contract1", "Contract3"]
    }
    response = client.post(path, json=input)
    assert response.json() == output


def test_simple2():
    input = [
        {"name": "Contract1", "start": 0, "duration": 5, "price": 10},
        {"name": "Contract2", "start": 3, "duration": 7, "price": 14},
        {"name": "Contract3", "start": 5, "duration": 9, "price": 8},
        {"name": "Contract4", "start": 5, "duration": 8, "price": 7},
        {"name": "Contract5", "start": 15, "duration": 9, "price": 8},
        {"name": "Contract6", "start": 16, "duration": 8, "price": 12},
    ]
    output = {
        "income": 30,
        "path": ["Contract1", "Contract3", "Contract6"]
    }
    response = client.post(path, json=input)
    assert response.json() == output
