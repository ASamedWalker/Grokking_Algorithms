"""This is the binary search algorithm.
   A lot of algorithms work only if they are sorted.
   It's runtime in terms of Big O is O(log n). 
   Linear search on the other hand is O(n).
"""
def binary_search(list, item):
  low = 0
  high = len(list) - 1
  while low <= high:
    mid = (low + high) // 2
    guess = list[mid]
    if guess == item:
      return mid
    if guess > item:
      high = mid - 1
    else:
      low = mid + 1
  return None
  # binary search algorithms runs on sorted group of list items
my_list = [1,3,5,7,9]
print(binary_search(my_list, 3))
print(binary_search(my_list, -1))
