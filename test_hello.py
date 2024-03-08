from predictions import app
import pytest
import json
import flask

@pytest.fixture
def client(): # From layman perspective this will act as a server, but not a server.
    return app.test_client()

def test_predictions(client):
    test_data = {
            "Gender": "Male",
            "Married": "Yes",
            "ApplicantIncome": 500000000,
            "LoanAmount": 5000,
            "Credit_History": 1.0
    }
    resp = client.post('/predict', json = test_data)
    assert resp.status_code == 200
    assert resp.json == {"loan_approval_status": "Accepted"}
