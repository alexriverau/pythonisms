from functools import wraps
from time import time
from generators import LinkedList


def display_result(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        original_value = func(*args, **kwargs)
        return f'Result: {original_value}'
    return wrapper


def function_timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        ms = (end_time - start_time) * 1000
        print(f'Time spent in {func.__name__}: {round(ms, 6)} milliseconds')
        return result
    return wrapper


@function_timer
@display_result
def sum_values(ll):
    current = ll.head
    total = 0

    while current:
        total += current.value
        current = current.next
    return total


if __name__ == '__main__':
    ll1 = LinkedList([1, 2, 3, 4, 5])
    ll2 = LinkedList([234235432, 5654534, 58695345, 456456.34, 98798, 123.34534])
    print(sum_values(ll1))
    print(sum_values(ll2))
