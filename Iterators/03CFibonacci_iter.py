# fibonacci series
class Fibonacci:
  def __init__(self, max_value):        # Constructor
    self.max_value = max_value
    self.current_value = 0
    self.next_value = 1
    
  def __iter__(self):           # iterable obj pass to iter()
    return self
    
  def __next__(self):           # iterator obj passed to next()
    result = self.current_value
    if result > self.max_value:
      raise StopIteration
    self.current_value, self.next_value = self.next_value, self.current_value + self.next_value
    return result

fibonacci_iterable = Fibonacci(10)
for i in fibonacci_iterable:
  print(i)  
