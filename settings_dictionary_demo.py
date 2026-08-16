# Basic dictionary creation, access, and updates.
def demo_basic_dict_operations():
    settings = {"theme": "dark", "language": "en"}
    print(settings["theme"])              # Access by key -> "dark"
    settings["notifications"] = "enabled" # Add a new key-value pair
    print(settings["notifications"])

# Different ways to iterate over a dictionary.
def demo_dict_iteration():
    settings = {"theme": "dark", "language": "en", "font_size": 14}
    # Iterating over keys only
    print("\nIterating over keys:")
    for key in settings:
        print(key, settings[key])
    # Iterating over key-value pairs (preferred, more readable)
    print("\nIterating over items:")
    for key, value in settings.items():
        print(key, "is set to", value)

# How to safely access a value with a default fallback
def demo_safe_get():
    settings = {"theme": "dark", "language": "en", "font_size": 14}
    # .get() avoids a KeyError if the setting doesn't exist
    print("\nSafe get:")
    print(settings.get("theme", "light"))          # existing key -> "dark"
    print(settings.get("auto_save", "disabled"))   # missing key -> "disabled" (no crash)

demo_basic_dict_operations()
demo_dict_iteration()
demo_safe_get()