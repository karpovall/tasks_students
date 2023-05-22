import pytest
import testlib

from mount import mount


class Case:
    def __init__(self, name: str, a: list[int], expected: bool):
        self._name = name
        self.a = a
        self.expected = expected

    def __str__(self) -> str:
        return 'test_{}'.format(self._name)


TEST_CASES = [
    Case(name='basic', a=[], expected=False),
    Case(name='negative', a=[1, 2, 3], expected=False),
    Case(name='zero_sum', a=[1, 2, 3, 0, -1], expected=True),
]


###################
# Structure asserts
###################


def test_banned_functions() -> None:
    assert not testlib.is_global_used(mount, 'sum')


###################
# Tests
###################


@pytest.mark.parametrize('test_case', TEST_CASES, ids=str)
def test_hello_world(test_case: Case) -> None:
    answer = mount(test_case.a)
    assert answer == test_case.expected
