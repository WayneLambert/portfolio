import heapq

# Create a list of square numbers between 1 and 10
square_nums = [num ** 2 for num in range(1, 11)]

# List of the 3 smallest items - ascending order
print(heapq.nsmallest(3, square_nums))

# List of the 3 largest items - ascending order
print(heapq.nlargest(3, square_nums)[::-1])

# List of the 3 largest items - descending order
print(heapq.nlargest(3, square_nums))

# Create a list of even numbers between 1 and 100
even_nums = [num for num in range(1, 101) if num % 2 == 0]

# List of the first 10 even numbers between 1-100 - ascending order
print(heapq.nsmallest(10, even_nums))

# Create a list of numbers between 1 and 1000 that are a multiple of 7
multiples_of_seven = [num for num in range(1, 1001) if num % 7 == 0]

# List of the last 10 numbers which are multiple of 7 between 1-1000 - ascending order
print(heapq.nlargest(10, multiples_of_seven)[::-1])

portfolio = [
    {'name': 'GOOGL', 'shares': 100, 'price': 1242.29},
    {'name': 'AMZN', 'shares': 35, 'price': 1739.84},
    {'name': 'TSLA', 'shares': 75, 'price': 242.56},
    {'name': 'AAPL', 'shares': 50, 'price': 219.89},
    {'name': 'FB', 'shares': 200, 'price': 180.09},
    {'name': 'MSFT', 'shares': 45, 'price': 139.54},
]

cheap = heapq.nsmallest(2, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(2, portfolio, key=lambda s: s['price'])

print(f"Cheap Shares\n '{cheap}")
print(f"Expensive Shares\n '{expensive}")
