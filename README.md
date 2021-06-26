# Assignment S7 - Scopes and Closures

### 1. Write a closure that takes a function and then check whether the function passed has a docstring with more than 50 characters. 50 is stored as a free variable (+ 4 tests) - 200
``` python
def scanfunc(scanlen: int) -> 'Function':
    """
    Closure that takes a function and checks if the function has a docstring with more than 50 characters.
    50 is stored as a free variable.
    """
    def doclength(fn: 'Function') -> 'True or False':
        """
        Inner Function that checks the docstring length.
        """
        if not isinstance(fn, Callable):
            raise TypeError("Expected function!")
        if len(fn.__doc__) > scanlen:
            return True
    return doclength
```

### 2. Write a closure that gives you the next Fibonacci number (+ 2 tests) - 100

``` python
def fibonacci() -> "Function":
    """
    Function that uses closure and gives you the next Fibonacci number.
    Tracks the old Fibonacci number using free variable.
    """
    n1, n2 = 1, 1
    count = 0

    def fibonaccinext() -> "Number":
        """
        Returns the next fibonacci number in the sequence.
        """
        nonlocal n1, n2, count
        count += 1
        if count <= 2:
            return n2
        n1, n2 = n2, n1+n2
        return n2
    return fibonaccinext
    
```


### 3. We wrote a closure that counts how many times a function was called. Write a new one that can keep a track of how many times add/mul/div functions were called, and update a global dictionary variable with the counts (+ 6 tests) - 250



``` python
func_count = {}

def counter() -> "Function":
    """
    Counter Function to count the number using free variables
    """
    counter = {}

    def count(func: 'Function', *args, **kwargs):
        """
        This function updates and keeps track of the number of times, 
        a function might be called.
        """
        if not isinstance(func, Callable):
            raise TypeError("Expected function!")
        counter[func.__name__] = counter.get(func.__name__, 0) + 1
        func_count[func.__name__] = counter[func.__name__]
        return func(*args, **kwargs)
    return count
    
```


### 4. Modify above such that now we can pass in different dictionary variables to update different dictionaries (+ 6 tests) - 250

``` python
def counter_users(user_dict: dict) -> "Function":
    """
    Function to count users using free variables.
    """
    counter = {}
    if not isinstance(user_dict, dict):
        raise TypeError('Expected Dictionary')

    def count(func: 'Function', *args, **kwargs):
        """
        This function updates and keeps track of the number of times, 
        a function might be called.
        """
        if not isinstance(func, Callable):
            raise TypeError("Expected function!")
        nonlocal counter
        counter[func.__name__] = counter.get(func.__name__, 0) + 1
        user_dict[func.__name__] = user_dict.get(
            func.__name__, 0) + 1
        return func(*args, **kwargs)
    return count

```


### Test Cases:

#### * 1a. test_doc_checker_scan():
Checks for docstring>50 in scan function
#### * 1b. test_doc_checker_fib():
Checks for docstring>50 in fibonacci function
#### * 1c. test_doc_checker_func():
Checks for docstring>50 in counter function
#### * 1d. test_doc_checker_parameter_type():
Checks for proper type in doc function
#### * 2a. test_fibonacci_boundary():
#### * 2b. test_fibonacci_random():
#### * 3a. test_func_add_count():
test case for addition in counter function
#### * 3b. test_func_mul_count():
test case for multiplication in counter function
#### * 3c. test_func_div_count():
test case for division in counter function
#### * 3d. test_func_print_count()
test case for print in counter function:
#### * 3e. test_func_count_parameter_type():
Checks for proper type in cuonter function
#### * 4a. test_func_count_add_custom():
test case for addition in custom counter function
#### * 4b. test_func_count_mul_custom():
test case for multiplication in custom counter function
#### * 4c. test_func_count_div_custom():
test case for division in custom counter function
#### * 4d. test_func_count_print_custom():
test case for print in custom counter function
#### * 4e. test_func_count_custom_parameter_type():
Checks for proper type in custom counter function


``` python

# 1. ScanFunc (4 Cases)

#1a
def test_doc_checker_scan():
    dcheck = session7.scanfunc(50)
    assert dcheck(session7.counter) == True, "Check the doc_check function for scan."
#1b
def test_doc_checker_fib():
    dcheck = session7.fibonacci()
    assert dcheck(session7.counter) == True, "Check the doc_check function for fib"
#1c
def test_doc_checker_func():
    dcheck = session7.func_count()
    assert dcheck(session7.counter) == True, "Check the doc_check function for func"
#1d
def test_doc_checker_parameter_type():
    with pytest.raises(TypeError):
        dc = session7.scanfunc()
        dc("No input")

# 2. Fibonacci (2 Cases)
#2a
def test_fibonacci_boundary():
    fib = session7.fibonacci()
    assert fib == 1, "Check Fibonacci Function"
    assert fib == 1, "Check Fibonacci Function"
    assert fib == 2, "Check Fibonacci Function"
#2b
def test_fibonacci_random():
    # Checking for 11th fibonacci number
    fib = session7.fibonacci()
    for i in range(10):
        fib
    assert fib == 89, "Check Fibonacci Function"


# 3. Function Counter (6 Cases)
#3a
def test_func_add_count():
    def add(a, b):
        return a+b
    fc = session7.counter()
    for _ in range(10):
        fc(add, 2, 5)
    assert session7.func_count['add'] == 10, "Check the func_count function."

#3b
def test_func_mul_count():
    def mul(a, b):
        return a*b
    fc = session7.counter()
    for _ in range(7):
        fc(mul, 2, 5)
    assert session7.func_count['mul'] == 7, "Check the func_count function."

#3c
def test_func_div_count():
    def div(a, b):
        return b and a/b
    fc = session7.counter()
    for _ in range(15):
        fc(div, 2, 5)
    assert session7.func_count['div'] == 15, "Check the func_count function."

#3d
def test_func_print_count():
    fc = session7.counter()
    for _ in range(3):
        fc(print, "Apple")
    assert session7.func_count['print'] == 3, "Check the func_count function."

#3e
def test_func_count_parameter_type():
    with pytest.raises(TypeError):
        fc = session7.counter()
        fc("This is not a function and should throw error!")
#3f

# 4. Custom Function Counter (6 Cases)

#4a
def test_func_count_add_custom():
    def add(a, b):
        return a+b
    dict_1 = dict()
    fc = session7.counter_users(dict_1)
    a, b, c, d = randint(1, 10, 4)
    for _ in range(a):
        fc(add, 2, 5)
    assert dict_1['add'] == a, "Check the func_count function."

    dict_2 = dict()
    fc_new = session7.counter_users(dict_2)
    a, b, c, d = randint(1, 10, 4)
    for _ in range(a):
        fc_new(add, 2, 5)
    assert dict_2['add'] == a, "Check the func_count function."

#4b
def test_func_count_mul_custom():
    def mul(a, b):
        return a*b
    dict_1 = dict()
    fc = session7.counter_users(dict_1)
    a, b, c, d = randint(1, 10, 4)
    for _ in range(b):
        fc(mul, 2, 5)
    assert dict_1['mul'] == b, "Check the func_count function."

    dict_2 = dict()
    fc_new = session7.counter_users(dict_2)
    a, b, c, d = randint(1, 10, 4)
    for _ in range(b):
        fc_new(mul, 2, 5)
    assert dict_2['mul'] == b, "Check the func_count function."

#4c
def test_func_count_div_custom():
    def div(a, b):
        return b and a/b
    dict_1 = dict()
    fc = session7.counter_users(dict_1)
    a, b, c, d = randint(1, 10, 4)
    for _ in range(c):
        fc(div, 2, 5)
    assert dict_1['div'] == c, "Check the func_count function."

    dict_2 = dict()
    fc_new = session7.counter_users(dict_2)
    a, b, c, d = randint(1, 10, 4)
    for _ in range(c):
        fc_new(div, 2, 5)
    assert dict_2['div'] == c, "Check the func_count function."

#4d
def test_func_count_print_custom():
    dict_1 = dict()
    fc = session7.counter_users(dict_1)
    a, b, c, d = randint(1, 10, 4)
    for _ in range(d):
        fc(print, "Apple")
    assert dict_1['print'] == d, "Check the func_count function."

    dict_2 = dict()
    fc_new = session7.counter_users(dict_2)
    a, b, c, d = randint(1, 10, 4)
    for _ in range(d):
        fc_new(print, "Apple")
    assert dict_2['print'] == d, "Check the func_count function."

#4e
def test_func_count_custom_parameter_type():
    with pytest.raises(TypeError):
        fc = session7.counter_users(1)

    with pytest.raises(TypeError):
        fc = session7.counter({})
        fc("This is not a function and should throw error!")
```
