import pytest

def test_web_routes_render(client):
    # Test Dashboard view
    res = client.get('/')
    assert res.status_code == 200
    assert b"TalentNexus" in res.data

    # Test Login view
    res = client.get('/login')
    assert res.status_code == 200
    assert b"Welcome to TalentNexus AI" in res.data

    # Test Register view
    res = client.get('/register')
    assert res.status_code == 200
    assert b"Register Your Organization" in res.data

    # Test ATS Kanban view
    res = client.get('/ats/kanban')
    assert res.status_code == 200
    assert b"Recruitment Pipeline Board" in res.data

    # Test Jobs list view
    res = client.get('/jobs')
    assert res.status_code == 200

    # Test Candidates list view
    res = client.get('/candidates')
    assert res.status_code == 200
