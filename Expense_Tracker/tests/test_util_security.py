from library.util import hash_password, check_password

def test_hash_and_check_password():
    pw = "secure123"
    hashed = hash_password(pw)
    assert hashed != pw
    assert check_password(pw, hashed)
    assert not check_password("wrongpass", hashed)