# Basic dictionary creation, access, and updates.
def demo_basic_dict_operations():
    contacts = {"Alice": "alice@example.com", "Bob": "555-1234"}
    print(contacts["Alice"])                  # Access by key -> "alice@example.com"
    contacts["Carol"] = "carol@example.com"   # Add a new key-value pair
    print(contacts["Carol"])

# Different ways to iterate over a dictionary.
def demo_dict_iteration():
    contacts = {"Alice": "alice@example.com", "Bob": "555-1234", "Carol": "carol@example.com"}
    # Iterating over keys only
    print("\nIterating over keys:")
    for name in contacts:
        print(name, contacts[name])
    # Iterating over key-value pairs (preferred, more readable)
    print("\nIterating over items:")
    for name, info in contacts.items():
        print(name, "->", info)

# How to safely access a value with a default fallback
def demo_safe_get():
    contacts = {"Alice": "alice@example.com", "Bob": "555-1234", "Carol": "carol@example.com"}
    # .get() avoids a KeyError if the contact doesn't exist
    print("\nSafe get:")
    print(contacts.get("Alice", "Not found"))   # existing key -> "alice@example.com"
    print(contacts.get("Dave", "Not found"))    # missing key -> "Not found" (no crash)

demo_basic_dict_operations()
demo_dict_iteration()
demo_safe_get()