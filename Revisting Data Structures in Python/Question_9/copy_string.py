# Program to copy a String as in python string are immutable and can be copied in various ways that are give below:

# Using String Slicing
def copy_string(original):
    copied = original[:]
    return copied

# Using the `str` constructor
def copy_string_constructor(original):
    copied = str(original)
    return copied

# Using the `+` operator
def copy_string_concatenation(original):
    copied = original + ''
    return copied

# Using `join` method
def copy_string_join(original):
    copied = ''.join(original)
    return copied

# Test the functions
original_string = "Hello, World!"
print("Original String:", original_string)

copied_string_slicing = copy_string(original_string)
copied_string_constructor = copy_string_constructor(original_string)
copied_string_concatenation = copy_string_concatenation(original_string)
copied_string_join = copy_string_join(original_string)

print("Copied String (Slicing):", copied_string_slicing)
print("Copied String (Constructor):", copied_string_constructor)
print("Copied String (Concatenation):", copied_string_concatenation)
print("Copied String (Join):", copied_string_join)
