import time
def timer(func):
"""A decorator that prints how long a function took to run.
Args:
func (callable): The function being decorated.
Returns:
callable: The decorated function.
"""

    # Define the wrapper function to return.
    def wrapper(*args, **kwargs):
    # When wrapper() is called, get the current time.
        t_start = time.time()
        # Call the decorated function and store the result.
        result = func(*args, **kwargs)
        # Get the total time it took to run, and print it.
        t_total = time.time() - t_start
        print('{} took {}s'.format(func.__name__, t_total))
    return result
return wrapper
