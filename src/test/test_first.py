"""
PYTESTS
"""

import pytest
from src.app import create_app


@pytest.fixture
def client():
    """
    Fixture
    :return:
    """
    app = create_app()

    app.config['TESTING'] = True

    with app.app_context():
        with app.test_client() as api_client:
            yield api_client


def test_first(client):
    """
    test of first
    :param client:
    :return: None
    """
    response = client.get('/api/v1.0/first')
    assert response.status_code == 200
