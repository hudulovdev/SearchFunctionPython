# Sample data
data = [
    {'name': 'John Doe', 'age': 25, 'city': 'New York'},
    {'name': 'Jane Smith', 'age': 30, 'city': 'Los Angeles'},
    {'name': 'Bob Johnson', 'age': 35, 'city': 'Chicago'},
    {'name': 'Alice Williams', 'age': 28, 'city': 'New York'},
    {'name': 'Michael Brown', 'age': 32, 'city': 'Los Angeles'},
]

def search(query):
    results = []
    for item in data:
        # Convert the item to lowercase for case-insensitive search
        item_lower = {key: str(value).lower() for key, value in item.items()}
        if query.lower() in item_lower.values():
            results.append(item)
    return results

# Example usage:
query = input("Enter search query: ")
search_results = search(query)

if search_results:
    print("Search results:")
    for result in search_results:
        print(result)
else:
    print("No results found.")
