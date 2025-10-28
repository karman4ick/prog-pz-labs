import hashlib
users = {
    "karma": {
        "password": hashlib.md5("123456".encode()).hexdigest(),
        "name": "karma karma karma"
    },
    "nikita": {
        "password": hashlib.md5("098765".encode()).hexdigest(),
        "name": "nikita nikita nikita"
    },
    "lol": {
        "password": hashlib.md5("06457".encode()).hexdigest(),
        "name": "lol lol lol"
    }
}
def authenticate():
    login = input("login: ").strip()
    password = input("password: ").strip()
    if login not in users:
        print("invalid login")
        return
    hashed_input = hashlib.md5(password.encode()).hexdigest()
    if hashed_input == users[login]["password"]:
        print("login ok")
    else:
        print("login failed")
authenticate()