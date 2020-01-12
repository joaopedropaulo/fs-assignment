from app.services.security import verify_password, get_password_hash

def test_get_password_hash_and_verify_password():
    hashed_p = get_password_hash("test")
    assert verify_password("test", hashed_p)
