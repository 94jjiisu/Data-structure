
"""
ArrayStack 클래스

class ArrayStack:
  LIFO Stack implementation using a Python list as underlying storage.
  
  def __init__(self):
  Create an empty stack.
  
  def __len__(self):
  Return the number of elements in the stack.
  
  def is_empty(self):
  Return True if the stack is empty.
  
  def push(self, e):
  Add element e to the top of the stack.
  
  def top(self):
  Return (but do not remove) the element at the top of the stack.
  Raise Empty exception if the stack is empty.
  
  def pop(self):
  Remove and return the element from the top of the stack (i.e., LIFO).
  Raise Empty exception if the stack is empty.
  
  """

class Empty(Exception):
"""Error attempting to access an element from an empty container."""
pass

class ArrayStack:
"""LIFO Stack implementation using a Python list as underlying storage."""

  def __init__(self):
    """Create an empty stack."""
    self._data = [] # nonpublic list instance

  def __len__(self):
    """Return the number of elements in the stack."""
    return len(self._data)

  
  def is_empty(self):
    """Return True if the stack is empty."""
    return len(self._data) == 0
  
  def push(self, e):
    """Add element e to the top of the stack."""
    self._data.append(e) # new item stored at end of list
    
    
  def top(self):
    """Return (but do not remove) the element at the top of the stack.
    Raise Empty exception if the stack is empty.
    """
    if self.is_empty():
      raise Empty('Stack is empty')
    return self._data[-1] # the last item in the list
  
  def pop(self):
    """Remove and return the element from the top of the stack (i.e., LIFO).
    Raise Empty exception if the stack is empty.
    """
    if self.is_empty():
      raise Empty('Stack is empty')
    return self._data.pop() # remove last item from list
  
  
  
 

# 예시1 - 문서 뒤집기

# 스택 생성
def reverse_file(filename):
  """Overwrite given file with its contents line-by-line reversed."""
  S = ArrayStack()
# 스택을 생성해서 S로 둔다.

# 스택에 라인 별로 문서 넣기
  original = open(filename)
  for line in original:
    S.push(line.rstrip('\n')) # we will re-insert newlines when writing
  original.close()
#파일에서 문서를 읽고 문서의 각 라인을 newline을 제거해서 스택에 넣는다.


# 스택에서 라인을 꺼내서 거꾸로 된 문서 생성
# now we overwrite with contents in LIFO order
  output = open(filename, 'w') # reopening file overwrites original
  while not S.is_empty():
    output.write(S.pop() + '\n') # re-insert newline characters
  output.close()
# 스택에서 꺼낼 때는 newline을 추가해서 문서 파일에 쓴다.



# 예시2 - 수식에서 괄호 문법 체크

 
  
