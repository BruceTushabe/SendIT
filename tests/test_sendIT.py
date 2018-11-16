
from flask import jsonify
from endpoints import app
import pytest

@pytest.fixture
def client():
        test_client = app.test_client()
        return test_client

class TestEndpoints():
        def test_createParcelOrder(self,client):
                client.post("/api/v1/parcel", data=jsonify({
               'parcelId':1,
               'name': 'car',
               'price': '$ 1000',
               'pickup': 'Germany',
               'destination': 'Kampala',
               'status':'delivered'
                }))
                response = app.test_client.get("/api/v1/parcel/1")
                assert response.status_code == 201






        


