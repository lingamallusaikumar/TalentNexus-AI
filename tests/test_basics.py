def test_app_health_endpoint(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json == {'status': 'healthy', 'service': 'talentnexus-ai'}

def test_api_health_endpoint(client):
    response = client.get('/api/v1/health')
    assert response.status_code == 200
    # In test environment, DB will be SQLite memory and should be healthy
    assert response.json['status'] == 'healthy'
    assert response.json['database'] == 'healthy'
