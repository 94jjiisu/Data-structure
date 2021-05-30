### 단방향 연결리스트 ###

# 노드 클래스
class _Node:
  def __init__(self, element=None, next=None):
    self._element = element # 노드에 저장되는 element 값
    self._next = next # 다음 노드로의 링크 (초기값은 None)
    
  def __str__(self):
    return str(self._element) # 출력 문자열 (print(node)에서 사용)

  
# 클래스 선언
class SinglyLinkedList:
  def __init__(self):
    self._head = None # 연결리스트의 가장 앞의 노드 (head)
    self._size = 0 # 리스트의 노드 개수
  
  def __len__(self):
    return self._size # len(A) = A의 노드 개수 리턴
  
  
  def print_list(self):
    v = self._head
    while (v):
      print(v._element, "->", end=" ")
      v = v._next
    print("None")
    
  def add_first(self, element):
    newest = self._Node(element, self._head) # 새 노드 생성
    self._head = newest
    self._size += 1
    
  def add_last(self, element):
    newest = self._Node(element) # 새 노드 생성
    if self._head == None: # empty list
      self._head = newest
    else:
      tail = self._head
      while tail._next != None:
        tail = tail._next
      tail._next = newest
    self._size += 1
    
  def remove_first(self):
    # head 노드의 값 리턴. empty list이면 None 리턴
    if self._head == None: # empty list
      return None
    element = self._head._element
    self._head = self._head._next
    self._size -= 1
    return element
  
  def remove_last(self):
    # tail 노드의 값 리턴
    # empty list이면 None 리턴
    if self._head == None:
      return None
    prev = None
    tail = self._head
    while tail._next != None:
      prev = tail
      tail = tail._next
    if prev == None:
      self._head = None
    else:
      prev._next = None
    self._size -= 1
    return tail._element
  
  
  def search(self, element):
    # element 값을 저장된 노드 리턴. 없으면 None 리턴
    v = self._head
    while v:
      if v._element == element: return v
      v = v._next
    return v
  
  def __iter__(self): # generator 정의
    v = self._head
    while v != None:
      yield v
      assert isinstance(v._next, object)
      v = v._next
      
  def search(self, element):
    for v in self:
      if v._element == element:
        return v
    return None
  
  def remove(self, element):
    # 노드 x를 제거한 후 True리턴. 제거 실패면 False 리턴
    x = self.search(element)
    if x == None or self._size == 0:
      return False
    if x == self._head:
      self.remove_first()
    else:
      prev = self._head
      while prev._next != x :
        prev = prev._next
      prev._next = x._next
      self._size -= 1
    return True
  
    
    
### 연결 스택 ###

# 클래스 선언
class Empty(Exception):
"""Error attempting to access an element from an empty container."""
pass

class LinkedStack:
"""LIFO Stack implementation using a singly linked list for storage."""

class _Node:
  """Lightweight, nonpublic class for storing a singly linked node."""
  __slots__ = '_element', '_next' # streamline memory usage
  
  def __init__(self, element, next): # initialize node's fields
    self._element = element # reference to user's element
    self._next = next # reference to next node
    
  def __init__(self):
    """Create an empty stack."""
    self._head = None # reference to the head node
    self._size = 0 # number of stack elements
    
  def __len__(self):
    """Return the number of elements in the stack."""
    return self._size
  
  def is_empty(self):
    """Return True if the stack is_empty."""
    return self._size == 0
  
  def push(self, e):
    """Add element e to the top of the stack."""
    self._head = self._Node(e, self._head) # create and link a new node
    self._size += 1
    
  def top(self):
    """Return (but do not remove) the element at the top of the stack.
    Raise Empty exception if the stack is_empty.
    """
    if self.is_empty():
      raise Empty('Stack is_empty')
    return self._head._element # top of stack is at head of list
  
  def pop(self):
    """Remove and return the element from the top of the stack (i.e., LIFO).
    Raise Empty exception if the stack is_empty.
    """
    if self.is_empty():
      raise Empty('Stack is_empty')
    answer = self._head._element
    self._head = self._head._next # bypass the former top node
    self._size -= 1
    return answer
  
  
 
### 연결 큐 ###

class Empty(Exception):
"""Error attempting to access an element from an empty container."""
pass

class LinkedQueue:
"""FIFO queue implementation using a singly linked list for storage."""

class _Node:
  """Lightweight, nonpublic class for storing a singly linked node."""
  __slots__ = '_element', '_next' # streamline memory usage
  
  def __init__(self, element, next):
    self._element = element
    self._next = next
    
  def __init__(self):
    """Create an empty queue."""
    self._head = None
    self._tail = None
    self._size = 0 # number of queue elements
    
  def __len__(self):
    """Return the number of elements in the queue."""
    return self._size
  
  def is_empty(self):
    """Return True if the queue is_empty."""
    return self._size == 0
  
  def first(self):
    """Return (but do not remove) the element at the front of the queue.
    Raise Empty exception if the queue is_empty.
    """
    if self.is_empty():
      raise Empty('Queue is_empty')
    return self._head._element # front aligned with head of list
  
  def dequeue(self):
    """Remove and return the first element of the queue (i.e., FIFO).
    Raise Empty exception if the queue is_empty.
    """
    if self.is_empty():
      raise Empty('Queue is_empty')
    if self._size == 1: # special case as queue is_empty
      self._tail = None # removed head had been the tail
    answer = self._head._element
    self._head = self._head._next
    self._size -= 1
    return answer
  
  def enqueue(self, e):
    """Add an element to the back of queue."""
    newest = self._Node(e, None) # node will be new tail node
    if self.is_empty():
      self._head = newest # special case: previously empty
    else:
      self._tail._next = newest
    self._tail = newest # update reference to tail node
    self._size += 1
    
    
