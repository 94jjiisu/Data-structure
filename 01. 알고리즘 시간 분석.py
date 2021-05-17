# O(1) 시간 알고리즘

def increment_one(a):
  return a+1


# O(logn) 시간 알고리즘

def number_of_bits(n):
  count = 0
  while n > 0:
    n = n // 2
    count += 1
   return count


# O(n) 시간 알고리즘

def find_max(data):
  """Return the maximum element from a nonempty Python list."""
  biggest = data[0]
  for val in data:
    if val > biggest:
      biggest = val
   return biggest


# O(n^2) 시간 알고리즘(누적 평균, Prefix Averages)

def prefix_average1(S):
  """Return list such that, for all j, A[j] equals average of S[0], ..., S[j]."""
  n = len(S)
  A = [0] * n # create new list of n zeros
  for j in range(n):
    total = 0 # begin computing S[0] + ... + S[j]
    for i in range(j + 1):
      total += S[i]
    A[j] = total / (j+1) # record the average
  return A


# O(n^2) 시간 알고리즘(누적 평균, Prefix Averages)

def prefix_average2(S):
  """Return list such that, for all j, A[j] equals average of S[0], ..., S[j]."""
  n = len(S)
  A = [0] * n # create new list of n zeros
  for j in range(n):
    A[j] = sum(S[0:j+1]) / (j+1) # record the average
  return A


# O(n) 시간 알고리즘(누적 평균, Prefix Averages)
# 반복되는 합산 연산을 없앰으로써 O(n) 시간 복잡도를 갖게 됨

def prefix_average3(S):
  """Return list such that, for all j, A[j] equals average of S[0], ..., S[j]."""
  n = len(S)
  A = [0] * n # create new list of n zeros
  total = 0 # compute prefix sum as S[0] + S[1] + ...
  for j in range(n):
    total += S[j] # update prefix sum to include S[j]
    A[j] = total / (j+1) # compute average based on current sum
  return A


# O(n^3) 시간 알고리즘(Nested Loop)
# 세 종류의 집합 분리(Three-Way Set Disjointness)

def disjoint1(A, B, C):
  """Return True if there is no element common to all three lists."""
  for a in A:
    for b in B:
      for c in C:
        if a == b == c:
          return False # we found a common value
  return True


# O(n^2) 시간 알고리즘
# 세 종류의 집합 분리(Three-Way Set Disjointness)

def disjoint2(A, B, C):
  """Return True if there is no element common to all three lists."""
  for a in A:
    for b in B:
      if a == b: # only check C if we found match from A and B
        for c in C:
          if a == c # (and thus a == b == c)
            return False # we found a common value
  return True # if we reach this, sets are disjoint


# O(n^2) 시간 알고리즘
# 집합 중복 체크(Element Uniqueness)

def unique1(S):
  """Return True if there are no duplicate elements in sequence S."""
  for j in range(len(S)):
    for k in range(j+1, len(S)):
      if S[j] == S[k]:
        return False # found duplicate pair
  return True # if we reach this, elements were unique


# O(nlogn) 시간 알고리즘
# 집합 중복 체크(Element Uniqueness)

def unique2(S):
  """Return True if there are no duplicate elements in sequence S."""
  temp = sorted(S) # create a sorted copy of S
  for j in range(1, len(temp)):
    if S[j-1] == S[j]:
      return False # found duplicate pair
  return True # if we reach this, elements were unique


# O(2^n)시간 알고리즘(피보나치 수열)

def fibonacci(k):
  if k <= 1: return k
  return fibonacci(k-1)+fibonacci(k-2)
