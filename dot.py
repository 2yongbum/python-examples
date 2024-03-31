class Dot(dict):
  """dot.notation access to dictionary attributes"""
  __getattr__= dict.__getitem__
  __setattr__= dict.__setitem__
  __delattr__= dict.__delitem__

  def __init__(self, dct={}):
    for key, value in dct.items():
      if hasattr(value, 'keys'):
        value = Dot(value)
      self[key] = value

  def __getattr__(self, k):
    if k not in self:
      self[k] = self.__class__()
    return self.get(k)

  def __getstate__(self):
    return self

  def __setstate__(self, state):
    self.update(state)
    self.__dict__ = self


class Node(Dot):
  def get_attr(self, attr):
    return None
  
  def __getattr__(self, attr):
    if attr not in self:
      self[attr] = self.get_attr(attr) or Node()
    return self.get(attr)
