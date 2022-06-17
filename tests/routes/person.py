import pytest
from http import HTTPStatus
from fastapi.testclient import TestClient


def test_nothing(client: TestClient, session):
    resp = client.get('/person/1')
    assert resp.status_code == HTTPStatus.NOT_FOUND
    assert resp.json()['detail'] == 'Person with this data not found'
