from app.services.token import create_access_token, get_username_from_access_token

def test_token_successful_creation_and_decoding() -> None:
    token = create_access_token(
        data={"sub": "test1"}
    )
    parsed_payload = get_username_from_access_token(token)

    assert parsed_payload == "test1"