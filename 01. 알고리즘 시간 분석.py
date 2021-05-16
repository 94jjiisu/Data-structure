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

