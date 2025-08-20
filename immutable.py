# integer, string, tuples, frozen set, boolean

# Example:

a = 5
first_location = id(a)
print(first_location)

a = 6
second_location = id(a)
print(second_location)

print(first_location == second_location)

# Output:
# True