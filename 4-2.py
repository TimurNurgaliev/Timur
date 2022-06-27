class ReversedList:
  def __init__(self, lst):
    self.l = list(reversed(lst))
     
  def __str__(self):
    return str(self.l)
