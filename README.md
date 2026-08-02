# Python Dictionary Demo
 
A small script demonstrating core Python `dict` operations: creation, access,
updates, iteration, and safe lookups.
 
## What it covers
 
- **Basic operations** — creating a dictionary, accessing values by key,
  and adding new key-value pairs.
- **Iteration** — looping over keys only vs. looping over key-value pairs
  with `.items()`.
- **Safe access** — using `.get()` with a default value to avoid a
  `KeyError` when a key might not exist.
## Usage
 
```bash
python dict_demo.py
```
 
### Expected output
 
```
Alice
alice@example.com
 
Iterating over keys:
Alice 26
Bob 31
Carol 28
 
Iterating over items:
Alice is 26 years old
Bob is 31 years old
Carol is 28 years old
 
Safe get:
26
0
```
 
## Requirements
 
- Python 3.x (no external dependencies)
## License
 
MIT
