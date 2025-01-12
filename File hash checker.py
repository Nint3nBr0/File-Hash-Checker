#imports modules to hashlib for hashing and os to check the file path
import hashlib
import os

# This saves the user input for the file and original hash that was found on the web
filename = input("Enter the path for the file: ")
original_hash = input("Enter the original file hash: ")

#This function checks the file in chunks to efficiently hash the file. 
def read_in_chunks(file_object, byte_size=4096):
    while True:
        file_data = file_object.read(byte_size)
        if not file_data:
            break
        yield file_data

#This function hashes the file that was input by the user
def file_hash():
    sha_256_hash = hashlib.sha256()
    with open(filename, 'rb') as file:
        for chunk in read_in_chunks(file):
            sha_256_hash.update(chunk)

    return sha_256_hash.hexdigest()

#This code checks if the file can be access or if it exists
if not os.path.exists(filename) or not os.access(filename, os.R_OK):
    print("File can not be accessed or does not exist")

#This posts the calculated Hash
calculated_hash = file_hash()
print(f"The file hash is : {calculated_hash}")

#This checks if the hash and the original hash are the same or if they are different
if calculated_hash == original_hash:
    print("The hashes are the same.")
else:
    print("These hashes are different.")
