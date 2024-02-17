from chalice.test import Client
from app import app

# create a variable
event = {
    "nome":"Eric",
    "idade":"30"
}

def test_index():
    with Client(app) as client:
        response = client.lambda_.invoke('invoke', event)
        assert response.payload == True
