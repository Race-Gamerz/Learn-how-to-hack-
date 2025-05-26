import zipfile
import itertools
import string

def crack_zip(zip_file, max_length=4):
    chars = string.ascii_letters + string.digits
    attempts = 0
    with zipfile.ZipFile(zip_file) as zf:
        for length in range(1, max_length + 1):
            for guess in itertools.product(chars, repeat=length):
                password = ''.join(guess)
                try:
                    zf.extractall(pwd=password.encode())
                    print(f"Password found: {password}")
                    return password
                except:
                    attempts += 1
    print("Password not found.")
    return None

zip_file = input("Enter ZIP file path: ")
crack_zip(zip_file)
