print('Это основной модуль main.py, его имя в процессе выполнения программы:', __name__)


from pack_1 import file11
from pack_2.pack_21 import file211

print('a =', file11.a)
print('b =', file211.b)
print('Dict:', file211.some_dict)