import pytest
from ..src.app import create_app


@pytest.fixture
def client():
    app = create_app()

    app.config['TESTING'] = True

    with app.app_context():
        with app.test_client() as client:

            yield client


def test_first(client):
    response = client.get('/api/v1.0/first')
    assert response.status_code == 200
