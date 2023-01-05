# reverse custom iterator
class ReverseIterable:   # ITERABLE:-An object, that one can iterate over and generates an Iterator when passed to iter() method
  def __init__(self, iterable):  # constructor
    self.iterable = iterable
    
  def __iter__(self):       # magic method for iteration
    return ReverseIterator(self.iterable) 

class ReverseIterator:      # ITERATOR:- An object, which is used to iterate over an iterable object using the __next__() method and  __next__() method,  returns next item of  object.
  def __init__(self, iterable):
    self.iterable = iterable
    self.index = len(iterable)
    
  def __next__(self):       # next metthod return next item of object
    if self.index == 0:
      raise StopIteration
    self.index -= 1
    return self.iterable[self.index]

reverse_iterable = ReverseIterable([1, 2, 3, 4])
for i in reverse_iterable:
  print(i)  
