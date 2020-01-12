from starlette.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_login_for_access_token_wrong_method():
    response = client.get("/token")
    assert response.status_code == 405 
    assert response.json() == {"detail": "Method Not Allowed"}

def test_login_for_access_token_no_credentials():
    response = client.post("/token", headers={}, json={})
    assert response.status_code == 422 
    assert response.json() == {"detail":[{"loc":["body","username"],"msg":"field required","type":"value_error.missing"},{"loc":["body","password"],"msg":"field required","type":"value_error.missing"}]}

def test_login_for_access_token_wrong_username():
    response = client.post("/token", headers={"Content-Type": "application/x-www-form-urlencoded"}, data={"username": "test", "password": "test"})
    assert response.status_code == 401 
    assert response.json() == {"detail":"Incorrect username or password"}

def test_login_for_access_token_wrong_password():
    response = client.post("/token", headers={"Content-Type": "application/x-www-form-urlencoded"}, data={"username": "user1", "password": "test"})
    assert response.status_code == 401 
    assert response.json() == {"detail":"Incorrect username or password"}

def test_login_for_access_token_successful():
    response = client.post("/token", headers={"Content-Type": "application/x-www-form-urlencoded"}, data={"username": "user1", "password": "pass1"})
    assert response.status_code == 200

def test_get_vehicles_for_user_bad_token():
    response = client.get("/vehicles", headers={"Authorization": "Bearer wrong_stuff"})
    assert response.status_code == 401 
    assert response.json() == {"detail": "Could not validate credentials"}

def test_get_vehicles_for_user_no_auth_header():
    response = client.get("/vehicles")
    assert response.status_code == 401 
    assert response.json() == {"detail": "Not authenticated"}