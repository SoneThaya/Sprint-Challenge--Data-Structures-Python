
class RingBuffer:

  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = []

  def append(self, item):
    # check to see if list is full  
    if len(self.storage) == self.capacity:
        # if True the item at current index is replaced by new item
        self.storage[self.current] = item
    else:
        # if False appends the item
        self.storage.append(item)
    # sets current to new oldest item
    self.current = (self.current + 1) % self.capacity

  def get(self):
    # returns the list
    return self.storage
    
    
