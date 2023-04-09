import functions
from data import my_dict
from classes import *


print ('This is executable file')

new_variable: int = 15


if __name__ == '__main__':
    print('The code below will fail if this file is an import module in another executable')
    print(functions.get_dubble_number(100))
    print(my_dict)
    MyClass()
    print(dir())