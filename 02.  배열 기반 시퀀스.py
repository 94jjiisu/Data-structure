# 동적 배열 구현

"""
DynamicArray 클래스 
class DynamicArray:
  def __init__(self): # 초기화
  def __len__(self):  # 길이
  def __getitem__(self, k): # 인덱스 k의 데이터 반환
  def _make_array(self, c): # 배열 생성, nonpublic utitity 
  def _resize(self, c): # 배열 크기 조절, nonpublic utitity 
  def append(self, obj):  # 데이터 추가  
  def remove(self, value):  # 데이터 삭제    
  def insert(self, k, value): # 데이터 삽입
  def reverse(self): # 데이터 순서 뒤집기
  def extend(self, data2): # 데이터 
"""


import ctypes                                      # provides low-level arrays

class DynamicArray:
  """A dynamic array class akin to a simplified Python list."""

  def __init__(self):
    """Create an empty array."""
    self._n = 0                                    # count actual elements
    self._capacity = 1                             # default array capacity
    self._A = self._make_array(self._capacity)     # low-level array
    
  def __len__(self):
    """Return number of elements stored in the array."""
    return self._n
    
  def __getitem__(self, k):
    """Return element at index k."""
    if not 0 <= k < self._n:
      raise IndexError('invalid index')
    return self._A[k]                              # retrieve from array
  
  def append(self, obj):
    """Add object to end of the array."""
    if self._n == self._capacity:                  # not enough room
      self._resize(2 * self._capacity)             # so double capacity
    self._A[self._n] = obj
    self._n += 1

  def _resize(self, c):                            # nonpublic utitity
    """Resize internal array to capacity c."""
    B = self._make_array(c)                        # new (bigger) array
    for k in range(self._n):                       # for each existing value
      B[k] = self._A[k]
    self._A = B                                    # use the bigger array
    self._capacity = c

  def _make_array(self, c):                        # nonpublic utitity
     """Return new array with capacity c."""   
     return (c * ctypes.py_object)()               # see ctypes documentation

  def insert(self, k, value):
    """Insert value at index k, shifting subsequent values rightward."""
    # (for simplicity, we assume 0 <= k <= n in this verion)
    if self._n == self._capacity:                  # not enough room
      self._resize(2 * self._capacity)             # so double capacity
    for j in range(self._n, k, -1):                # shift rightmost first
      self._A[j] = self._A[j-1]
    self._A[k] = value                             # store newest element
    self._n += 1

  def remove(self, value):
    """Remove first occurrence of value (or raise ValueError)."""
    # note: we do not consider shrinking the dynamic array in this version
    for k in range(self._n):
      if self._A[k] == value:              # found a match!
        for j in range(k, self._n - 1):    # shift others to fill gap
          self._A[j] = self._A[j+1]
        self._A[self._n - 1] = None        # help garbage collection
        self._n -= 1                       # we have one less item
        return                             # exit immediately
    raise ValueError('value not found')    # only reached if no match
  
  def reverse(self):
    # write your code
    if self._n == 0:
      raise IndexError('invalid index')
    #if self._n % 2 == 0:
    start = 0
    end = self._n -1
    while start < end:
      self._A[start], self._A[end] = self._A[end], self._A[start]
      start += 1
      end -= 1
    

  def extend(self, data2):
    # write your code
    for i in range(data2._n):
      if self._n == self._capacity:
        self._resize(2 * self._capacity)
      self._A[self._n] = data2[i]
      self._n += 1
"""
  def extend(self, data2):
      for i in range(data2._n):
        self._A[self._n] = data2[i]
        self._n += 1
      self._resize(2 * self._capacity)
"""
      
  def __repr__(self):
    mylist = ", ".join(str(self._A[i]) for i in range(self._n))
    return "[" + mylist + "]"

data1 = DynamicArray()
for i in range(10):
  data1.append(i)
print("data1 : ", data1)

data2 = DynamicArray()
for i in range(10, 15, 1):
  data2.append(i)
print("data2 : ", data2)
data1.extend(data2)
print("extended : ", data1)

data1.reverse()
print("reversed : ", data1)



      
# append 성능분석
# Python의 append 구현이 amortized 𝚶(𝟏)인지 확인해보자!

import sys
from time import time
try:
  maxN = int(sys.argv[1])
except:
  maxN = 10000000
from time import time # import time function from time module
def compute_average(n):
  """Perform n appends to an empty list and return average time elapsed."""
  data = []
  start = time() # record the start time (in seconds)
  for k in range(n):
    data.append(None)
  end = time() # record the end time (in seconds)
  return (end - start) / n # compute average per operation

n = 10
while n <= maxN:
print('Average of {0:.3f} for n {1}'.format(compute_average(n)*1000000, n))
n *= 10


# 문자열 생성 - 문서에서 알파벳만 추출하려 할 때 다음 코드를 개선하는 방법

letters = '' # start with empty string
for c in document:
  if c.isalpha():
    letters += c # concatenate alphabetic character
    
# 1
temp = [] # start with empty list
for c in document:
  if c.isalpha():
    temp.append(c) # append alphabetic character
letters = .join(temp) # compose overall result

# 2
letters = ''.join([c for c in document if c.isalpha()])

# 3
letters = ''.join(c for c in document if c.isalpha())
