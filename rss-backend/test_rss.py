import pytest
import rss

@pytest.fixture
def client():
    rss.app.config['TESTING'] = True
    client = rss.app.test_client()
    yield client

def test_get_rss_en(client):
    response = client.get('/rss/en')
    assert response.status_code == 200
    data = response.get_json()
    assert 'articles' in data
    assert data['articles'].__len__() > 0
    assert 'logo' in data

def test_get_rss_es(client):
    response = client.get('/rss/es')
    assert response.status_code == 200
    data = response.get_json()
    assert 'articles' in data
    assert data['articles'].__len__() > 0
    assert 'logo' in data

def test_translate_text():
    assert rss.translate_text('Hello') == 'Hola'

def test_404_invalid_route(client):
    response = client.get('/invalid-route')
    assert response.status_code == 404
