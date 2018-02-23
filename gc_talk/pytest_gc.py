import pytest
import gc


@pytest.fixture(autouse=True)
def garbage_detect(request):
    # Clean up all objects
    gc.set_debug(0)
    gc.collect()

    # Save garbage and run test
    gc.set_debug(gc.DEBUG_SAVEALL)
    yield

    # Invoke the garbage collector
    gc.collect()

    # Check that there is no garbage
    garbage_expected = request.node.get_marker('garbage')

    if not garbage_expected:
        assert len(gc.garbage) == 0
