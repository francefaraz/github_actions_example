import pytest
import json
from app import app

@pytest.fixture
def client():
    """Create a test client for the Flask application."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_endpoint(client):
    """Test the home endpoint."""
    response = client.get('/')
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert data['message'] == 'Welcome to the Backend API'
    assert data['status'] == 'running'
    assert data['version'] == '1.0.0'

def test_health_check(client):
    """Test the health check endpoint."""
    response = client.get('/health')
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert data['status'] == 'healthy'
    assert data['service'] == 'backend'

def test_get_data(client):
    """Test the GET /api/data endpoint."""
    response = client.get('/api/data')
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert 'data' in data
    assert isinstance(data['data'], list)
    assert len(data['data']) == 3
    
    # Check structure of first item
    first_item = data['data'][0]
    assert 'id' in first_item
    assert 'name' in first_item
    assert 'value' in first_item

def test_create_data_success(client):
    """Test successful POST /api/data endpoint."""
    test_data = {
        'name': 'Test Item',
        'value': 150
    }
    
    response = client.post('/api/data', 
                          data=json.dumps(test_data),
                          content_type='application/json')
    
    assert response.status_code == 201
    
    data = json.loads(response.data)
    assert data['message'] == 'Data created successfully'
    assert 'item' in data
    assert data['item']['name'] == 'Test Item'
    assert data['item']['value'] == 150

def test_create_data_no_data(client):
    """Test POST /api/data endpoint with no data."""
    response = client.post('/api/data')
    assert response.status_code == 400
    
    data = json.loads(response.data)
    assert data['error'] == 'No data provided'

def test_create_data_empty_json(client):
    """Test POST /api/data endpoint with empty JSON."""
    response = client.post('/api/data',
                          data=json.dumps({}),
                          content_type='application/json')
    
    assert response.status_code == 201
    
    data = json.loads(response.data)
    assert data['item']['name'] == 'New Item'
    assert data['item']['value'] == 0
