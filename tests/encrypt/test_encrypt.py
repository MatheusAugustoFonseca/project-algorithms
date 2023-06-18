from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    # pass
    assert encrypt_message("teste", 3) == "set_et"
    assert encrypt_message("teste", 2) == "ets_et"
    assert encrypt_message("", 2) == ""
    with pytest.raises(TypeError):
        encrypt_message(2, 2)
    with pytest.raises(TypeError):
        encrypt_message("teste", "teste")
