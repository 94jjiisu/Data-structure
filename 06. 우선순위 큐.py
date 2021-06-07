### _Item 클래스 ###

class _Item:
  """Lightweight composite to store priority queue items."""
  __slots__ = '_key', '_value'

  def __init__(self, k, v):
    self._key = k
    self._value = v
  
  def __lt__(self, other):
    return self._key < other._key # compare items based on their keys

  def __repr__(self):
    return '({0},{1})'.format(self._key, self._value)
  
  
### Priority Queue Base 클래스 ###

from ..exceptions import Empty
class PriorityQueueBase:
  """Abstract base class for a priority queue."""
  
  def is_empty(self): # concrete method assuming abstract len
    """Return True if the priority queue is empty."""
    return len(self) == 0
  
  def __len__(self):
    """Return the number of items in the priority queue."""
    raise NotImplementedError('must be implemented by subclass')
    
  def add(self, key, value):
    """Add a key-value pair."""
    raise NotImplementedError('must be implemented by subclass')
    
  def min(self):
    """Return but do not remove (k,v) tuple with minimum key.
    Raise Empty exception if empty.
    """
    raise NotImplementedError('must be implemented by subclass')
    
  def remove_min(self):
    """Remove and return (k,v) tuple with minimum key.
    Raise Empty exception if empty.
    """
    raise NotImplementedError('must be implemented by subclass')
    
  
  
### 정렬되지 않은 우선순위 큐 클래스 ###

from .priority_queue_base import PriorityQueueBase
from ..04. 연결리스트_2.py import PositionalList ## 파일이름 유의
from ..exceptions import Empty

class UnsortedPriorityQueue(PriorityQueueBase): # base class defines _Item
  """A min-oriented priority queue implemented with an unsorted list."""
  
  def __init__(self):
    """Create a new empty Priority Queue."""
    self._data = PositionalList()
    
  def __len__(self):
    """Return the number of items in the priority queue."""
    return len(self._data)
  
  def _find_min(self):
    """Return Position of item with minimum key."""
    if self.is_empty(): # is_empty inherited from base class
      raise Empty('Priority queue is empty')
    small = self._data.first()
    walk = self._data.after(small)
    while walk is not None:
      if walk.element() < small.element():
        small = walk
      walk = self._data.after(walk)
    return small
  
  def add(self, key, value):
    """Add a key-value pair."""
    self._data.add_last(self._Item(key, value))
    
  def min(self):
    """Return but do not remove (k,v) tuple with minimum key.
    Raise Empty exception if empty.
    """
    p = self._find_min()
    item = p.element()
    return (item._key, item._value)
  
  def remove_min(self):
    """Remove and return (k,v) tuple with minimum key.
    Raise Empty exception if empty.
    """
    p = self._find_min()
    item = self._data.delete(p)
    return (item._key, item._value)
  
  
  
### 정렬된 우선순위 큐 클래스 ###

