import heapq
li = [5, 70, 34, 67, 87, 9, 2, 1, 4]
# Without heapq
print(f"Without heapq: {li}")

# With heapq - This doesn't sort list elements
heapq.heapify(li)
print(f"After heapify: {li}")