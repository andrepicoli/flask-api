import pytest
from app.main import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_create_product(client):
    response = client.post('/api/products', json={
        'name': 'Laptop',
        'price': 1500,
        'description': 'A high-end gaming laptop'
    })
    
    assert response.status_code == 201
    json_data = response.get_json()
    assert json_data['name'] == 'Laptop'
    assert json_data['price'] == 1500
    assert json_data['description'] == 'A high-end gaming laptop'
    assert 'id' in json_data

def test_get_product(client):
    create_response = client.post('/api/products', json={
        'name': 'Smartphone',
        'price': 800,
        'description': 'A flagship smartphone'
    })
    
    json_data = create_response.get_json()
    product_id = json_data['id']

    get_response = client.get(f'/api/products/{product_id}')
    assert get_response.status_code == 200

    product_data = get_response.get_json()
    assert product_data['name'] == 'Smartphone'
    assert product_data['price'] == 800
    assert product_data['description'] == 'A flagship smartphone'

def test_get_non_existent_product(client):
    response = client.get('/api/products/9999')
    assert response.status_code == 404
    json_data = response.get_json()
    assert json_data['message'] == 'Product not found'
