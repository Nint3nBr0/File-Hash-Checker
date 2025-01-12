import hashlib
import os

filename = input("Enter the path for the file: ")
original_hash = input("Enter the original file hash: ")
def read_in_chunks(file_object, byte_size=4096):
    while True:
        file_data = file_object.read(byte_size)
        if not file_data:
            break
        yield file_data

def file_hash():
    sha_256_hash = hashlib.sha256()
    with open(filename, 'rb') as file:
        for chunk in read_in_chunks(file):
            sha_256_hash.update(chunk)

    return sha_256_hash.hexdigest()

if not os.path.exists(filename) or not os.access(filename, os.R_OK):
    print("File can not be accessed or does not exist")

calculated_hash = file_hash()
print(f"The file hash is : {calculated_hash}")

if calculated_hash == original_hash:
    print("The hashes are the same.")
else:
    print("These hashes are different.")