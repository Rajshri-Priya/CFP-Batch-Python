
class Characters:
  def __init__(self, string):
    self.string = string
    self.index = 0
  def __iter__(self):
    return self
    
  def __next__(self):
    if self.index >= len(self.string):
      raise StopIteration
    result = self.string[self.index]
    self.index += 1
    return result

characters_iterable = Characters('abcdefg')
for c in characters_iterable:
  print(c)  