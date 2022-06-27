class ReversedList:
  def __init__(self, lst):
    self.list = list(reversed(lst))
     
  def __str__(self):
    return str(self.list)
    
  def __getitem__(self, i):
    return self.list[i]
    
  def __len__(self):
    return len(self.list)
  
  

rl = ReversedList([10, 20, 30])
for i in range(len(rl)):
  print(rl[i])
