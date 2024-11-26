# Dictionary to store book data
borrowed_books = {}

# Prompt user for input
print("Enter the borrowed books' data. Type 'end' to stop.")

# Collect book data from the user
while True:
    title = input("Enter the book title: ")
    if title.lower() == "end":
        break  # Stop input if 'end' is entered
    
    days = input(f"Enter the number of days the book '{title}' was borrowed: ")
    try:
        days = int(days)  # Ensure days is an integer
    except ValueError:
        print("Please enter a valid number of days.")
        continue  # Skip to the next iteration if input is invalid

    # Add or update the book in the dictionary
    if title in borrowed_books:
        borrowed_books[title] += days
    else:
        borrowed_books[title] = days

# Set for unique book titles
unique_titles = set(borrowed_books.keys())

# Functions for analysis
def get_most_borrowed(data):
    most_borrowed = max(data.items(), key=lambda item: item[1])
    return most_borrowed

def get_least_borrowed(data):
    least_borrowed = min(data.items(), key=lambda item: item[1])
    return least_borrowed

def calculate_average(data):
    total_days = sum(data.values())
    total_books = len(data)
    if total_books > 0:
        return total_days / total_books
    return 0

def sort_books_by_days(data):
    sorted_books = sorted(data.items(), key=lambda item: item[1], reverse=True)
    return sorted_books

# Perform analysis
if borrowed_books:  # Check if there are any books entered
    most_borrowed = get_most_borrowed(borrowed_books)
    least_borrowed = get_least_borrowed(borrowed_books)
    average_days = calculate_average(borrowed_books)
    sorted_books = sort_books_by_days(borrowed_books)

    # Display results
    print(f"\nMost Borrowed Book: '{most_borrowed[0]}' with {most_borrowed[1]} days")
    print(f"Least Borrowed Book: '{least_borrowed[0]}' with {least_borrowed[1]} days")
    print(f"Average Borrowing Duration: {average_days:.2f} days")
    print("\nUnique Titles of Borrowed Books:")
    for title in unique_titles:
        print(f"- {title}")
    print("\nBooks Sorted by Borrowing Duration:")
    for title, days in sorted_books:
        print(f"{title}: {days} days")
else:
    print("No data entered.")