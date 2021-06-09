### 맵 ###

# 맵의 사용 예시
## 단어 개수 세기

# 문서가 들어있는 파일 이름
import sys
filename = sys.argv[1]

# 문서를 단어 단위로 분리하고, 맵에 저장
freq = {}
  for piece in open(filename).read().lower().split():
  # only consider alphabetic characters within this piece
  word = ''.join(c for c in piece if c.isalpha())
    if word: # require at least one alphabetic character
    freq[word] = 1 + freq.get(word, 0)

# 가장 많이 나타나는 단어를 찾아서 출력
max_word = ''
max_count = 0
  for (w,c) in freq.items(): # (key, value) tuples represent (word, count)
  if c > max_count:
    max_word = w
    max_count = c
print('The most frequent word is', max_word)
print('Its number of occurrences is', max_count)


### 정렬되지 않은 테이블 맵 구현 ###

# MutableMapping 클래스에는 Map 에서 필요한 기본 메소드가 정의되어 있음
# MutableMapping 클래스에는 Abstract Method가 있다는 가정 하에 Concrete Method가 구현되어 있음

# __getitem__ 이 있다는 가정 하에 구현

def __contains__ (self, k):
  try:
    self[k] # access via __getitem__ (ignore result)
    return True
  except KeyError:
    return False # attempt failed

# __getitem__과 __setitem__이 있다는 가정 하에 구현

def setdefault(self, k, d):
  try:
    return self[k] # if __getitem__ succeeds, return value
  except KeyError: # otherwise:
    self[k] = d # set default value with __setitem__
    return d # and return that newly assigned value
  
  
# MapBase 클래스
# MapBase 클래스에는 Map 구현에 공통으로 필요한 _Item 이 정의

from collections import MutableMapping
class MapBase(MutableMapping):
  """Our own abstract base class that includes a nonpublic _Item class."""
  
  
# _Item 클래스

class _Item:
  """Lightweight composite to store key-value pairs as map items."""
  __slots__ = '_key', '_value'
  
  def __init__(self, k, v):
    self._key = k
    self._value = v
    
  def __eq__(self, other):
    return self._key == other._key # compare items based on their keys
  
  def __ne__(self, other):
    return not (self == other) # opposite of __eq__
  
  def __lt__(self, other):
    return self._key < other._key # compare items based on their keys
  
  
  
### UnsortedTableMap 클래스

# (키, 값) 아이템을 정렬되지 않은 순서로 리스트로 관리하는 맵

from .map_base import MapBase
class UnsortedTableMap(MapBase):
  """Map implementation using an unordered list."""
  
  def __init__(self):
    """Create an empty map."""
    self._table = [] # list of _Item's
    
  def __getitem__(self, k):
    """Return value associated with key k (raise KeyError if not found)."""
    for item in self._table:
      if k == item._key:
        return item._value
    raise KeyError('Key Error: ' + repr(k))
    
  def __setitem__(self, k, v):
    """Assign value v to key k, overwriting existing value if present."""
    for item in self._table:
      if k == item._key: # Found a match:
        item._value = v # reassign value
         return # and quit
    # did not find match for key
    self._table.append(self._Item(k,v))
    
  def __delitem__(self, k):
    """Remove item associated with key k (raise KeyError if not found)."""
    for j in range(len(self._table)):
      if k == self._table[j]._key: # Found a match:
      self._table.pop(j) # remove item
      return # and quit
    raise KeyError('Key Error: ' + repr(k))
    
  def __len__(self):
    """Return number of items in the map."""
    return len(self._table)
  
  def __iter__(self):
    """Generate iteration of the map's keys."""
    for item in self._table:
      yield item._key # yield the KEY
      
  
