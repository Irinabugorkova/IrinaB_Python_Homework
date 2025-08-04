import pytest
from IrinaB_Python_Homework.Тренировка.урок4.string_processor import StringProcessor


@pytest.mark.parametrize("text, output", [
    ("hello", "Hello."),
    ("hello.", "Hello."),
    ("Hello", "Hello.")
    ])
def test_process_capitalization_and_period(text, output):
    assert StringProcessor.process(text) == output


@pytest.mark.parametrize("text, output", [
    ("", "."),
    ("   ", "   .")
     ])
def test_process_empty_and_spaces(text, output):
    assert StringProcessor.process(text) == output
