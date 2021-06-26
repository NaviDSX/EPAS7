import pytest
from numpy.random import randint
import session7
import os
import inspect
import re
import test_session7

README_CONTENT_CHECK_FOR = [
    'dict',
    'fibonacci',
    'Function',
    'counter',
    'docstring',
    'add',
    'mul',
    'closure'
]


CHECK_FOR_THINGS_NOT_ALLOWED = []


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    readme = open("README.md", "r", encoding="utf8")
    readme_words = readme.read().split()
    readme.close()
    assert len(
        readme_words) >= 300, "Make your README.md file interesting! Add atleast 500 words"


def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            print(c)
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You haven't well described your README.md file"


def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session7, inspect.isfunction)
    for function in functions:
        assert len(re.findall(
            '([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_function_count():
    functions = inspect.getmembers(test_session7, inspect.isfunction)
    assert len(functions) > 15, 'Low test cases'


def test_function_repeatations():
    functions = inspect.getmembers(test_session7, inspect.isfunction)
    names = []
    for function in functions:
        names.append(function)
    assert len(names) == len(set(names)), 'Repeating test cases...'


def test_function_doc_string():
    '''
    Test case to check whether the functions have docstrings or not.
    '''
    functions = inspect.getmembers(session7, inspect.isfunction)
    for function in functions:
        assert function[1].__doc__


def test_function_annotations():
    '''
    Test case to check whether the functions have annotations or not.
    '''
    functions = inspect.getmembers(session7, inspect.isfunction)
    for function in functions:
        assert function[1].__annotations__


def test_doc_checker():
    dcheck = session7.scanfunc(50)
    assert dcheck(session7.counter) == True, "Check the doc_check function for scan."

def test_doc_checker_fib():
    dcheck = session7.fibonacci()
    assert dcheck(fibonacci) == True, "Check the doc_check function for fib"


def test_doc_checker_parameter_type():
    with pytest.raises(TypeError):
        dc = session7.scanfunc()
        dc("No input")


def test_fibonacci():
    fib = session7.fibonacci()
    assert fibonacci() == 1, "Check Fibonacci Function"
    assert fibonacci() == 1, "Check Fibonacci Function"
    assert fibonacci() == 2, "Check Fibonacci Function"
    fib = session7.fibonacci()
    for i in range(10):
        fibonacci()
    # Checking for 11th fibonacci number
    assert fibonacci() == 89, "Check Fibonacci Function"


def test_func_count():
    def add(a, b):
        return a+b

    def mul(a, b):
        return a*b

    def div(a, b):
        return b and a/b
    fc = session7.counter()
    for _ in range(10):
        fc(add, 2, 5)
    for _ in range(7):
        fc(mul, 2, 5)
    for _ in range(15):
        fc(div, 2, 5)
    for _ in range(3):
        fc(print, "Apple")

    assert session7.func_count['add'] == 10, "Check the func_count function."
    assert session7.func_count['mul'] == 7, "Check the func_count function."
    assert session7.func_count['div'] == 15, "Check the func_count function."
    assert session7.func_count['print'] == 3, "Check the func_count function."


def test_func_count_parameter_type():
    with pytest.raises(TypeError):
        fc = session7.counter()
        fc("This is not a function and should throw error!")


def test_func_count_custom():
    def add(a, b):
        return a+b

    def mul(a, b):
        return a*b

    def div(a, b):
        return b and a/b

    dict_1 = dict()
    fc = session7.counter_users(dict_1)

    a, b, c, d = randint(1, 10, 4)

    for _ in range(a):
        fc(add, 2, 5)
    for _ in range(b):
        fc(mul, 2, 5)
    for _ in range(c):
        fc(div, 2, 5)
    for _ in range(d):
        fc(print, "Apple")

    assert dict_1['add'] == a, "Check the func_count function."
    assert dict_1['mul'] == b, "Check the func_count function."
    assert dict_1['div'] == c, "Check the func_count function."
    assert dict_1['print'] == d, "Check the func_count function."

    dict_2 = dict()
    fc_new = session7.counter_users(dict_2)

    a, b, c, d = randint(1, 10, 4)

    for _ in range(a):
        fc_new(add, 2, 5)
    for _ in range(b):
        fc_new(mul, 2, 5)
    for _ in range(c):
        fc_new(div, 2, 5)
    for _ in range(d):
        fc_new(print, "Apple")

    assert dict_2['add'] == a, "Check the func_count function."
    assert dict_2['mul'] == b, "Check the func_count function."
    assert dict_2['div'] == c, "Check the func_count function."
    assert dict_2['print'] == d, "Check the func_count function."


def test_func_count_custom_parameter_type():
    with pytest.raises(TypeError):
        fc = session7.counter_users(1)

    with pytest.raises(TypeError):
        fc = session7.counter({})
        fc("This is not a function and should throw error!")
