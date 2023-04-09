print('This is module:', __name__)


from ..file21 import another_some_func


b: int = 4242

some_dict: dict[int, str] = {1: 'A',
                             2: 'B',
                             3: 'C'}

r = another_some_func(b)