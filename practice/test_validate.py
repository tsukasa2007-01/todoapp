import pytest
from validate import is_valid_title, validate_title


def test_normal_title():
    assert is_valid_title("牛乳を買う") == True


def test_empty_is_false():
    assert is_valid_title("") == False


def test_spaces_only_is_false():
    assert is_valid_title("   ") == False


def test_101_chars_is_false():
    assert is_valid_title("あ" * 101) == False


def test_100_chars_is_true():
    assert is_valid_title("あ" * 100) == True


def test_validate_title_strips_spaces():
    assert validate_title("  牛乳を買う  ") == "牛乳を買う"


def test_validate_title_empty_raises():
    with pytest.raises(ValueError):
        validate_title("")


def test_validate_title_too_long_raises():
    with pytest.raises(ValueError):
        validate_title("あ" * 101)
