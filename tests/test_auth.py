import json

def test_register_user(client, app):
    data = {
        'email': 'test@example.com',
        'password': 'password123',
        'first_name': 'Test',
        'last_name': 'User',
        'role': 'Candidate',
        'organization_name': 'Test Org'
    }
    response = client.post('/api/v1/auth/register', 
                           data=json.dumps(data), 
                           content_type='application/json')
    assert response.status_code == 201
    assert 'token' in response.json

def test_login_user(client, app):
    # Register first
    data = {
        'email': 'test2@example.com',
        'password': 'password123',
        'first_name': 'Test2'
    }
    client.post('/api/v1/auth/register', data=json.dumps(data), content_type='application/json')
    
    # Login
    login_data = {
        'email': 'test2@example.com',
        'password': 'password123'
    }
    response = client.post('/api/v1/auth/login', 
                           data=json.dumps(login_data), 
                           content_type='application/json')
    assert response.status_code == 200
    assert 'token' in response.json
    assert response.json['user']['email'] == 'test2@example.com'

def test_get_current_user(client, app):
    data = {
        'email': 'test3@example.com',
        'password': 'password123',
        'first_name': 'Test3'
    }
    register_response = client.post('/api/v1/auth/register', 
                                    data=json.dumps(data), 
                                    content_type='application/json')
    token = register_response.json['token']
    
    response = client.get('/api/v1/auth/me', 
                          headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == 200
    assert response.json['email'] == 'test3@example.com'
