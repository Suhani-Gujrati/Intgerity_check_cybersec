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
print(calculate_sha256("example.txt"))
