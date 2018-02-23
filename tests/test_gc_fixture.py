import pytest
from gc_talk.pytest_gc import garbage_detect


def test_no_garbage():
    val = 10
    other_val = val


@pytest.mark.garbage
def test_garbage():
    x = []
    y = []
    x.append(y)
    y.append(x)
