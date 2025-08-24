from loading2 import loading


def test_loading_decorator_basic():
    @loading()
    def dummy():
        return 'ok'
    assert dummy() == "ok"
