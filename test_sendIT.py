
from flask import jsonify
from sendIT_endpoints import app
import pytest

@pytest.fixture
def client():
        test_client = app.test_client()
        return test_client

class TestEndpoints():
        def test_createParcelOrder(self,client):
                response = client.post("/api/v1/parcel", data=jsonify({
               'parcelId':1,
               'name': 'car',
               'price': '$ 1000',
               'pickup': 'Germany',
               'destination': 'Kampala',
               'status':'delivered'
                }))
                assert response.status_code == 201






        


