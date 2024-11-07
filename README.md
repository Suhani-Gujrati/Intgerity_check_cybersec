# SHA-256 Integrity Check Script

This Python script calculates the SHA-256 hash of a file and verifies its integrity by comparing the calculated hash with an expected hash value. It is useful for file integrity checking, where you want to ensure that a file has not been tampered with or corrupted.

## Features
- Calculate the SHA-256 hash of a file.
- Verify the integrity of the file by comparing its hash with a pre-defined expected hash.
- Works with any file type (text, binary, etc.).

## Prerequisites
- Python 3.x (Tested with Python 3.6+)
- `hashlib` module (pre-installed with Python standard library)

## Installation

1. Clone this repository to your local machine using Git:
   ```bash
   git clone https://github.com/your-username/sha256-integrity-check.git
   ```

2. Navigate to the project directory:
   ```bash
   cd sha256-integrity-check
   ```

3. Ensure you have Python installed on your system. You can check by running:
   ```bash
   python --version
   ```

## Usage

### 1. Calculate SHA-256 hash of a file

To calculate the SHA-256 hash of a file, you can use the `calculate_sha256(file_path)` function. Pass the path of the file as an argument, and it will return the hash in hexadecimal format.

#### Example:
```python
file_path = "example.txt"  # Replace with your file path
print(calculate_sha256(file_path))
```

### 2. Verify file integrity

The `verify_integrity(file_path, expected_hash)` function compares the calculated hash of a file with an expected hash. If the hashes match, it indicates that the file is intact (i.e., it hasn’t been modified or corrupted). If the hashes differ, an integrity failure is indicated.

#### Example:
```python
file_to_check = "example.txt"  # Path to your file
expected_hash = "e3ecbe786207d09675637ec85a9a0a21d4f19a2d74ea0717f7d0766d9fd86264"  # Replace with the initial hash
verify_integrity(file_to_check, expected_hash)
```

### 3. Full example:

Here’s the full code example:

```python
import hashlib

def calculate_sha256(file_path):
    """Calculate SHA-256 hash of a file."""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def verify_integrity(file_path, expected_hash):
    """Verify the integrity of a file by comparing its SHA-256 hash with an expected hash."""
    calculated_hash = calculate_sha256(file_path)  # Calculate the current hash
    print(f"Calculated SHA-256 hash of '{file_path}': {calculated_hash}")  # Show the calculated hash
    if calculated_hash == expected_hash:
        print("Integrity check passed!")
    else:
        print("Integrity check failed.")

if __name__ == "__main__":
    file_to_check = "example.txt"  # Path to your sample file
    
    # Set this value based on the original file's content
    expected_hash = "e3ecbe786207d09675637ec85a9a0a21d4f19a2d74ea0717f7d0766d9fd86264"  # Replace with the initial hash

    print(f"Expected SHA-256 hash of '{file_to_check}': {expected_hash}")
    
    # Verify integrity by checking the file against the expected hash
    verify_integrity(file_to_check, expected_hash)

    # Optionally, print the calculated hash for verification
    print(calculate_sha256("example.txt"))
```

### 4. Expected output:
```text
Expected SHA-256 hash of 'example.txt': e3ecbe786207d09675637ec85a9a0a21d4f19a2d74ea0717f7d0766d9fd86264
Calculated SHA-256 hash of 'example.txt': e3ecbe786207d09675637ec85a9a0a21d4f19a2d74ea0717f7d0766d9fd86264
Integrity check passed!
```

If the file's content changes, the calculated hash will not match the expected hash, and the output will be:
```text
Integrity check failed.
```

## How It Works
- **Hashing**: The script reads the file in binary mode and uses the SHA-256 algorithm (from Python's `hashlib` library) to compute the hash.
- **Comparison**: After calculating the file's hash, it compares the result with the provided expected hash.
- **Integrity Verification**: If both hashes match, it confirms that the file's integrity is intact. Otherwise, it flags the file as potentially corrupted or altered.

## File Structure

```
/sha256-integrity-check
│
├── example.txt              # Example file to check (replace with your own)
├── sha256_integrity_check.py # Python script
└── README.md                # This README file
```

## Contributing

1. Fork this repository to your GitHub account.
2. Clone your fork to your local machine.
3. Create a new branch:
   ```bash
   git checkout -b my-feature-branch
   ```
4. Make your changes, then commit and push:
   ```bash
   git commit -am 'Add my feature'
   git push origin my-feature-branch
   ```
5. Create a pull request to merge your changes into the main repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

This README file covers how to use the script, provides examples, and includes a basic explanation of how it works. Make sure to adjust the file names and paths as per your project.
