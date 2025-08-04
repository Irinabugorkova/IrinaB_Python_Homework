import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
def test_capitalize_whis_none():
    with pytest.raises(AttributeError):
        assert string_utils.capitalize(None)


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected_result", [
    ("   Hello!", "Hello!"),
    ("nospace", "nospace")
])
def test_trim_positive(input_str, expected_result):
    assert string_utils.trim(input_str) == expected_result


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected_result", [
    ("", ""),
    ("     ", "")
])
def test_trim_negative(input_str, expected_result):
    assert string_utils.trim(input_str) == expected_result


@pytest.mark.parametrize("input_str", [None])
def test_trim_with_none(input_str):
    with pytest.raises(AttributeError):
        string_utils.trim(input_str)


@pytest.mark.positive
@pytest.mark.parametrize("input_str, simbol", [
    ("skypro", "s"),
    ("hello", "e"),
    ("test123", "1")
])
def test_contains_positive(input_str, simbol):
    assert string_utils.contains(input_str, simbol) is True


@pytest.mark.negative
@pytest.mark.parametrize("input_str, simbol", [
    ("skypro", "z"),
    ("", "a"),
    ("hello", "")
])
def test_contains_negative(input_str, simbol):
    assert string_utils.contains(input_str, simbol) is False


@pytest.mark.positive
@pytest.mark.parametrize("input_str, simbol, expected_result", [
    ("Ирина", "рина", "И"),
    ("Привет", "ет", "Прив"),
    ("test123", "123", "test")
])
def test_delete_symbol_positive(input_str, simbol, expected_result):
    assert string_utils.delete_symbol(input_str, simbol) == expected_result


@pytest.mark.negative
@pytest.mark.parametrize("input_str, simbol, expected_result", [
    ("Ирина", "", "Ирина"),
    ("Привет", "К", "Привет"),
    ("", "123", "")
])
def test_delete_symbol_negative(input_str, simbol, expected_result):
    assert string_utils.delete_symbol(input_str, simbol) == expected_result
