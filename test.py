from app import generate_list


def test_generate_list():
    assert generate_list()[0] == "liste 1"
