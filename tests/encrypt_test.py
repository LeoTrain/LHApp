from cryptography.fernet import Fernet

def generate_key():
  key = Fernet.generate_key()
  with open("data/secret.key", "wb") as key_file:
    key_file.write(key)

def load_key():
  return open("data/secret.key", "rb").read()

def encrypt_data(data, key):
  f = Fernet(key)
  return f.encrypt(data.encode())

def decrypt_data(encrypted_data, key):
  f = Fernet(key)
  return f.decrypt(encrypted_data).decode()

def save_encrypted_credentials(credentials, file_path, key):
    with open(file_path, "wb") as file:
        for user, pwd in credentials.items():
            encrypted_user = encrypt_data(user, key)
            encrypted_pwd = encrypt_data(pwd, key)
            file.write(encrypted_user + b',' + encrypted_pwd + b'\n')

def load_encrypted_credentials(file_path, key):
    credentials = {}
    with open(file_path, "rb") as file:
        for line in file:
            encrypted_user, encrypted_pwd = line.strip().split(b',')
            user = decrypt_data(encrypted_user, key)
            pwd = decrypt_data(encrypted_pwd, key)
            credentials[user] = pwd
    return credentials

def check_credentials(username, password, credentials):
    return credentials.get(username) == password

def add_user(username, password, file_path, key):
    encrypted_user = encrypt_data(username, key)
    encrypted_pwd = encrypt_data(password, key)
    with open(file_path, "ab") as file:
        file.write(encrypted_user + b',' + encrypted_pwd + b'\n')
      
def main():
    file_path = 'data/encrypted_credentials.txt'
    key = load_key()
    
    # generate_key()
    
    credentials = load_encrypted_credentials(file_path, key)
    
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    # add_user(username, password, file_path, key)
    # print("User added successfully")
    
    if check_credentials(username, password, credentials):
      print("Access granted")
    else:
      print("Access denied")

if __name__ == "__main__":
    main()
