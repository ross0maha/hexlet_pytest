import pytest
from hexlet_pytest.stack import stack


def test_stack1():
    stack = []
    stack.append('one')
    stack.append('two')

    assert stack.pop() == 'two'


def test_stack2():
    stack = []
    stack.append('one')
    stack.append('two')

    stack.pop()
    assert stack.pop() == 'one'


def test_emptiness():
    stack = []
    assert not stack
    stack.append('one')
    assert bool(stack)  # not not stack

    stack.pop()
    assert not stack


def test_pop_with_empty_stack():
    stack = []
    # проверить что вызывается конкретное исключение можно с помощью
    # конструкции with pytest.raises()
    # если внутри блока вызовется исключение, то тест будет пройден
    with pytest.raises(IndexError):
        stack.pop()
