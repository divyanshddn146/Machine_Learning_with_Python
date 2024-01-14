import regex as re

strings = input("Enter comma-separated string: ")

# Input validation
if "," not in strings:
    print("Please enter a valid comma-separated string.")
else:
    list1 = strings.split(",")

    sorted_strings = sorted(list1, key=lambda x: (re.sub('\d+', '', x), int(re.sub('\D', '', x))) if any(c.isdigit() for c in x) else x)

    print(sorted_strings)
