from nose.tools import assert_true, assert_false

from src.throttler.throttle import Throttle


def test_1_1():
    throttle = Throttle(max_messages=1, time_window=1)
    assert_true(throttle.accept(0))
    assert_false(throttle.accept(0))
    assert_true(throttle.accept(1))


def test_should_consider_window_open_at_left():
    throttle = Throttle(max_messages=2, time_window=3)
    assert_true(throttle.accept(0))
    assert_true(throttle.accept(2))
    assert_true(throttle.accept(3))


def test_n_equals_t_allows_one_per_time_unit():
    for n in range(10, 200):
        throttle = Throttle(n, n)
        for i in range(100):
            assert_true(throttle.accept(i))


def test_from_example():
    example = """
1547222542000010 pass
1547222542000010 pass
1547222542000012 pass
1547222542000014 pass
1547222542000014 pass
1547222542000014 fail
1547222542000015 fail
1547222542000020 fail
1547222542000037 pass
1547222542000039 pass
    """
    throttle = Throttle(max_messages=5, time_window=20)
    for (t, r) in [l.split(' ') for l in example.splitlines()[1:-1]]:
        assert throttle.accept(int(t)) == (r == 'pass')
