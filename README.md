# Python Dictionary Basics

A set of small demo functions covering common dictionary operations in Python, shown across two different examples.

## Files
- **dictionary_basics.py** — dictionary operations using a people/ages example
- **settings_dictionary_demo.py** — the same operations applied to an app settings example

## What's covered
- **Basic operations**: creating a dictionary, accessing values by key, adding new key-value pairs
- **Iteration**: looping over keys only vs. looping over key-value pairs with `.items()`
- **Safe access**: using `.get()` with a default fallback to avoid a `KeyError` on missing keys

## How to run
```bash
python dictionary_basics.py
python settings_dictionary_demo.py
```

## What I learned
- Dictionaries store data as key-value pairs and support fast lookups by key
- `.items()` is more readable than looping over keys and indexing separately
- `.get(key, default)` is safer than `dict[key]` when a key might not exist
- The same dictionary patterns apply naturally across different real-world contexts (people data vs. config/settings data)
