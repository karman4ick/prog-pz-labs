import hashlib
def generate_file_hashes(*file_paths):
    hashes = {}
    for file_path in file_paths:
        try:
            with open(file_path, 'rb') as file:
                file_data = file.read()
                sha256_hash = hashlib.sha256(file_data).hexdigest()
                hashes[file_path] = sha256_hash
        except FileNotFoundError:
            print(f'File "{file_path}" not found')
        except IOError:
            print(f'File "{file_path}" read error')
    return hashes
result = generate_file_hashes("apache_logs.txt")
print(result)