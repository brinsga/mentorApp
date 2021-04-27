import pytest
from .hello import func

def test_answer():
    assert func(4) == 5
