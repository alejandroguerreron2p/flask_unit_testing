from main import create_app
import pytest
from api_dict import test_data

@pytest.fixture()
def app():
    app = create_app({
        "TESTING": True
    })
    yield app

@pytest.fixture()
def client(app):
    return app.test_client()