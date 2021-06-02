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
    
    
    
### 원형 연결리스트 ###

class Empty(Exception):
  """Error attempting to access an element from an empty container."""
pass

class CircularQueue:
  """Queue implementation using circularly linked list for storage."""
  
class _Node:
  """Lightweight, nonpublic class for storing a singly linked node."""
  __slots__ = '_element', '_next' # streamline memory usage
  def __init__(self, element, next):
    self._element = element
    self._next = next
    
  def __init__(self):
    """Create an empty queue."""
    self._tail = None # will represent tail of queue
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
    head = self._tail._next
    return head._element
  
  def dequeue(self):
    """Remove and return the first element of the queue (i.e., FIFO).
    Raise Empty exception if the queue is_empty.
    """
    if self.is_empty():
      raise Empty('Queue is_empty')
    oldhead = self._tail._next
    if self._size == 1: # removing only element
      self._tail = None # queue becomes empty
    else:
      self._tail._next = oldhead._next # bypass the old head
    self._size -= 1
    return oldhead._element
  
  def enqueue(self, e):
    """Add an element to the back of queue."""
    newest = self._Node(e, None) # node will be new tail node
    if self.is_empty():
      newest._next = newest # initialize circularly
    else:
      newest._next = self._tail._next # new node points to head
    self._tail._next = newest # old tail points to new node
    self._tail = newest # new node becomes the tail
    self._size += 1
    
  def rotate(self):
    """Rotate front element to the back of the queue."""
    if self._size > 0:
      self._tail = self._tail._next # old head becomes new tail
  
  
  
### 양방향 연결리스트 ###


  
class _Node:
  """Lightweight, nonpublic class for storing a doubly linked node."""
  __slots__ = '_element', '_prev', '_next' # streamline memory
  
  def __init__(self, element, prev, next): # initialize node's fields
    self._element = element # user's element
    self._prev = prev # previous node reference
    self._next = next # next node reference
    
class _DoublyLinkedBase:
  """A base class providing a doubly linked list representation."""
  
  def __init__(self):
    """Create an empty list."""
    self._header = self._Node(None, None, None)
    self._trailer = self._Node(None, None, None)
    self._header._next = self._trailer # trailer is after header
    self._trailer._prev = self._header # header is before trailer
    self._size = 0 # number of elements
    
  def __len__(self):
    """Return the number of elements in the list."""
    return self._size
  
  def is_empty(self):
    """Return True if list is_empty."""
    return self._size == 0
  
  def _insert_between(self, e, predecessor, successor):
    """Add element e between two existing nodes and return new node."""
    newest = self._Node(e, predecessor, successor) # linked to neighbors
    predecessor._next = newest
    successor._prev = newest
    self._size += 1
    return newest
  
  def _delete_node(self, node):
    """Delete nonsentinel node from the list and return its element."""
    predecessor = node._prev
    successor = node._next
    predecessor._next = successor
    successor._prev = predecessor
    self._size -= 1
    element = node._element # record deleted element
    node._prev = node._next = node._element = None # deprecate node
    return element # return deleted element
  
  
### 연결 덱 ###

from .doubly_linked_base import _DoublyLinkedBase
class Empty(Exception):
  """Error attempting to access an element from an empty container."""
  pass

class LinkedDeque(_DoublyLinkedBase): # note the use of inheritance
  """Double-ended queue implementation based on a doubly linked list."""
  
  def first(self):
    """Return (but do not remove) the element at the front of the deque.
    Raise Empty exception if the deque is_empty.
    """
    if self.is_empty():
      raise Empty("Deque is_empty")
    return self._header._next._element # real item just after header
  
  def last(self):
    """Return (but do not remove) the element at the back of the deque.
    Raise Empty exception if the deque is_empty.
    """
    if self.is_empty():
      raise Empty("Deque is_empty")
    return self._trailer._prev._element # real item just before trailer
  
  def insert_first(self, e):
    """Add an element to the front of the deque."""
    self._insert_between(e, self._header, self._header._next) # after header
    
  def insert_last(self, e):
    """Add an element to the back of the deque."""
    self._insert_between(e, self._trailer._prev, self._trailer) # before trailer
    
  def delete_first(self):
    """Remove and return the element from the front of the deque.
    Raise Empty exception if the deque is_empty.
    """
    if self.is_empty():
      raise Empty("Deque is_empty")
    return self._delete_node(self._header._next) # use inherited method
  
  def delete_last(self):
    """Remove and return the element from the back of the deque.
    Raise Empty exception if the deque is_empty.
    """
    if self.is_empty():
      raise Empty("Deque is_empty")
    return self._delete_node(self._trailer._prev) # use inherited method
  
  
  
  ### 원형 양방향 연결 덱 ###
  
class _Node:
  """Lightweight, nonpublic class for storing a doubly linked node."""
  __slots__ = '_element', '_prev', '_next' # streamline memory
  
  def __init__(self, element, prev, next): # initialize node's fields
    self._element = element # user's element
    self._prev = prev # previous node reference
    self._next = next # next node reference
    
  def __str__(self): # modified
    return str(self._element) # modified
  
class _CircularDoublyLinkedBase:
  """A base class providing a doubly linked list representation."""
  
  def __init__(self):
    """Create an empty list."""
    self._header = self._Node(None, None, None)
    self._header._next = self._header # modified
    self._header._prev = self._header # modified
    self._size = 0 # number of elements
    
  def __iter__(self): # generator 정의
    v = self._header._next
    while v != self._header:
      yield v
      assert isinstance(v._next, object)
      v = v._next
      
  def __str__(self): # 연결 리스트의 값을 print 출력
    return " -> ".join(str(v) for v in self)
