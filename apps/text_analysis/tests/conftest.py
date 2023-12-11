import pytest


@pytest.fixture(scope="function")
def text_to_analyse():
    s = "lorem ipsum " * 50
    return s.strip()


@pytest.fixture(scope="function")
def dirty_text():
    return "This is %;some di!ty to @na#.]se"
