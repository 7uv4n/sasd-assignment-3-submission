# Function to Hash the passwords

import hashlib

# Function to compute SHA-256 hash
def hashEncode(data):
    # Create a SHA-256 hash object
    sha256_hash = hashlib.sha256()
    
    # Update the hash object with the bytes of the data
    sha256_hash.update(data.encode('utf-8'))
    
    # Retrieve the hexadecimal digest
    hex_digest = sha256_hash.hexdigest()
    
    return hex_digest




