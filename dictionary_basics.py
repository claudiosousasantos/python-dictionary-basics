#  Basic dictionary creation, access, and updates.
def demo_basic_dict_operations():
    person = {"name": "Alice", "age": 30}
    print(person["name"])          # Access by key -> "Alice"

    person["email"] = "alice@example.com"  # Add a new key-value pair
    print(person["email"])

#Different ways to iterate over a dictionary.
def demo_dict_iteration():
    ages = {"Alice": 26, "Bob": 31, "Carol": 28}

    # Iterating over keys only
    print("\nIterating over keys:")
    for name in ages:
        print(name, ages[name])

    # Iterating over key-value pairs (preferred, more readable)
    print("\nIterating over items:")
    for name, age in ages.items():
        print(name, "is", age, "years old")

#How to safely access a value with a default fallback
def demo_safe_get():
    ages = {"Alice": 26, "Bob": 31, "Carol": 28}

    # .get() avoids a KeyError if the key doesn't exist
    print("\nSafe get:")
    print(ages.get("Alice", 0))     # existing key -> 26
    print(ages.get("Dave", 0))      # missing key -> 0 (no crash)



demo_basic_dict_operations()
demo_dict_iteration()
demo_safe_get()