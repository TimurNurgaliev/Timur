class Point:
  def __init__(self, x , y):
    self.x = x
    self.y = y
  def __eq__(other):
     if self.x == other.x and self.y == other.y:
       return True
     return False

    def __ne__(other):
      if self.x != other.x and self.y != other.y:
        return True
      return False

    
p1 = Point(1, 2)
p2 = Point(5, 6)

if p1 == p2:
    print("Equal True")
else:
    print("Equal False")

if p1 != p2:
    print("Not equal True")
else:
    print("Not equal False")
