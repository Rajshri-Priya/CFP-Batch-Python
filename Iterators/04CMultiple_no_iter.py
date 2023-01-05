# multiple of number
class Multiples:
  def __init__(self, multiple, max_value):  # constructor
    self.multiple = multiple
    self.max_value = max_value
    self.current_value = multiple
    
  def __iter__(self):
    return self
    
  def __next__(self):
    if self.current_value > self.max_value:
      raise StopIteration
    result = self.current_value
    self.current_value += self.multiple
    return result

multiples_iterable = Multiples(5, 25)
for i in multiples_iterable:
  print(i)  # Output: 5 10 15 20 25
