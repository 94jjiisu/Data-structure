### 단방향 연결리스트 ###

# 노드 클래스
class _Node:
  def __init__(self, element=None, next=None):
    self._element = element # 노드에 저장되는 element 값
    self._next = next # 다음 노드로의 링크 (초기값은 None)
    
  def __str__(self):
    return str(self._element) # 출력 문자열 (print(node)에서 사용)
