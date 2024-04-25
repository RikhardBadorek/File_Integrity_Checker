import os
import hashlib

def calculate_directory_hash(directory_path):
    sha256_hash = hashlib.sha256()
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            with open(file_path, "rb") as f:
                while True:
                    data = f.read(65536)
                    if not data:
                        break
                    sha256_hash.update(data)
    return sha256_hash.hexdigest()

def check_integrity(directory_path, stored_hash):
    if not os.path.exists(directory_path) or not os.path.isdir(directory_path):
        print("This directory does not exist")
        return

    calculated_hash = calculate_directory_hash(directory_path)
    print(f"Calculated SHA-256 hash of the directory: {calculated_hash}")

    if calculated_hash == stored_hash:
        print("Hash-values match, nothing detected.")
    else:
        print("WARNING: Hash-values don't match. Check for any undetected attacks.")

def main():
    stored_hash = input("Enter the stored SHA-256 hash of the directory: ")
    directory_path = input("Enter the directory path to check the integrity: ")
    check_integrity(directory_path, stored_hash)

if __name__ == "__main__":
    main()

# TEST HASH d15e23f9ee4dc8884484fec2347a430cdc84703879da62181377f87cd52d65ed
# FILE PATH TO TEST: C:\Users\rikhard\Desktop\PROTECT THIS DIRECTORY
# THIS HASH WOULD BE STORED IN A VERY SECURE PLACE
