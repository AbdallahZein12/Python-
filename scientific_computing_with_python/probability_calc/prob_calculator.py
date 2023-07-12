import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    if not kwargs:
      raise TypeError("Atleast one keyword arg is required")
    else:
      self.contents = [key for key, value in kwargs.items() if value >= 1 for _ in range(value)]

  def draw(self,num_of_balls):
    if num_of_balls > len(self.contents):
      self.contents.clear()
      return self.contents
    else:
      return [self.contents.pop(random.randrange(len(self.contents))) for _ in range(num_of_balls)]
    


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  m = 0
  for i in range(num_experiments):
    another_hat = copy.deepcopy(hat)
    balls_drawn = another_hat.draw(num_of_balls=num_balls_drawn)
    balls_req = sum([1 for k,v in expected_balls.items() if balls_drawn.count(k) >= v]) 
    m += 1 if balls_req == len(expected_balls) else 0

  return m / num_experiments
