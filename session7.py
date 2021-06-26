from collections import Callable


def scanfunc(scanlen: int) -> 'function':
    """
    Closure that takes a function and then check whether the function passed has a docstring with more than 50 characters. 50 is stored as a free variable.
    """
    def doclength(fn: 'function') -> 'True or False':
        """
        Inner function that checks the docstring length.
        """
        if not isinstance(fn, Callable):
            raise TypeError("Expected function!")
        if len(fn.__doc__) > scanlen:
            return True
    return doclength


def fibonacci() -> "function":
    """
    function that uses closure and gives you the next Fibonacci number.
    Tracks the old Fibonacci number using free variable.
    """
    n1, n2 = 1, 1
    count = 0

    def fibonaccinext():
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


func_count = {}


def counter() -> "function":
    """
    Counter function to count the number using free variables
    """
    counter = {}

    def count(func: 'function', *args, **kwargs):
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


def counter_users(user_dict: dict) -> "function":
    """
    function to count users using free variables.
    """
    counter = {}
    if not isinstance(user_dict, dict):
        raise TypeError('Expected Dictionary')

    def count(func: 'function', *args, **kwargs):
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
