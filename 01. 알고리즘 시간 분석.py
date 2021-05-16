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
