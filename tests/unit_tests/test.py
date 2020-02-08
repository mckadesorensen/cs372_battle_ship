from src.main import test
import pytest

@pytest.fixture
def unit_test():
    assert test() == 'test'