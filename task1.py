steps = list(map(int, input("Enter the number of steps taken each day, separated by spaces: ").split()))

highest_steps = max(steps)
lowest_steps = min(steps)

average_steps = sum(steps) / len(steps)

sorted_steps = sorted(steps, reverse=True)

print("\nDaily Steps Tracker Results:")
print(f"Highest step count: {highest_steps}")
print(f"Lowest step count: {lowest_steps}")
print(f"Average daily step count: {average_steps:.2f}")
print(f"Steps in descending order: {sorted_steps}")
# Test Case Input: