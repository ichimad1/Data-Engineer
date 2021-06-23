def run_n_times(n):
  """Define and return a decorator"""
  def decorator(func):
    def wrapper(*args, **kwargs):
      for i in range(n):
        func(*args, **kwargs)
    return wrapper
  return decorator

# Modify the print() function to always run 20 times
print = run_n_times(20)(print)

print('What is happening?!?!')
