# Homework 5 - Lists and Tuples
# Lina Almajidi

# -----------------------------
# List Exercise
# -----------------------------

items = ["coffee", "pen", "notebook", "phone", "badge", "backpack"]

# Print the items in the list
print("Items in my list:")
for item in items:
    print(item)

# Print the first two items using a slice
first_two = items[:2]
print(f"\nThe first two items in the list are: {first_two[0]}, {first_two[1]}")

# Print the middle two items using a slice (for 6 items, middle is index 2 and 3)
middle_two = items[2:4]
print(f"The middle two items in the list are: {middle_two[0]}, {middle_two[1]}")

# Print the first and last items using indexes
print(f"The first and last items in the list are: {items[0]}, {items[-1]}")


# -----------------------------
# Tuple Exercise
# -----------------------------

menu = ("pizza", "burger", "salad", "soup", "pasta")

print("\nOriginal menu:")
for food in menu:
    print(food)

# Revised menu (replace two items)
revised_menu = ("pizza", "tacos", "salad", "ramen", "pasta")

print("\nRevised menu:")
for food in revised_menu:
    print(food)
