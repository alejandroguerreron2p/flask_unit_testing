from main import create_app
from service.hash_book_repository import HashBookRepository
from service.api_dict import test_data
import pytest

@pytest.fixture()
def app():
    app = create_app({
        "TESTING": True
    })
    yield app

@pytest.fixture()
def client(app):
    return app.test_client()
