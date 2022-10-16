"""This is a selection sort algorithm.
   It's not very fast. Quicksort is a faster 
   sorting algorithm that only takes O(nlogn) time.
   We using selection_sort here to find the smallest to the highest.
"""
def find_smallest(arr):
  smallest = arr[0]
  smallest_index = 0
  for i in range(1, len(arr)):
    if arr[i] < smallest:
      smallest = arr[i]
      smallest_index = i
  return smallest_index

# Selection Sort Algorithm
def selection_sort(arr):
  newArr = []
  for i in range(len(arr)):
    smallest = find_smallest(arr)
    newArr.append(arr.pop(smallest))
  return newArr

print(selection_sort([5, 3, 6, 2, 10]))