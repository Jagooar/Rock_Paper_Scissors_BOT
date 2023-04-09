print('This is module', __name__)


from .file12 import num


def some_func(n: int) -> float:
    return (n + n) / n**n


result = some_func(num)