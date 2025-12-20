import sqlite3
import hashlib
DB_NAME = "users.db"
def get_password_hash(password):
    return hashlib.sha256(password.encode()).hexdigest()
def create_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            login TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            full_name TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    print(f"Data base '{DB_NAME}' created successfully.")
def add_user(login, password, full_name):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    hashed_password = get_password_hash(password)
    try:
        cursor.execute('''
            INSERT INTO users (login, password, full_name) 
            VALUES (?, ?, ?)
        ''', (login, hashed_password, full_name))
        conn.commit()
        print(f"User {login} successfully added.!")
    except sqlite3.IntegrityError:
        print(f"Error: user '{login}' already exists.")
    finally:
        conn.close()
def update_user_password(login, new_password):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    hashed_password = get_password_hash(new_password)
    cursor.execute('''
        UPDATE users 
        SET password = ? 
        WHERE login = ?
    ''', (hashed_password, login))
    if cursor.rowcount > 0:
        conn.commit()
        print("Password updated successfully.")
    else:
        print(f"User with login '{login}' not found.")
    conn.close()
def authenticate_user(login, password):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    input_hash = get_password_hash(password)
    cursor.execute('''
        SELECT password FROM users WHERE login = ?
    ''', (login,))
    result = cursor.fetchone()
    conn.close()
    if result:
        stored_hash = result[0]
        if stored_hash == input_hash:
            print(f"Authenticated user '{login}' successfully.")
            return True
    print("Error: wrong login or password.")
    return False
if __name__ == "__main__":
    create_db()
    while True:
        print("\n--- MENU ---")
        print("1. Add a new user")
        print("2. Refresh password")
        print("3. Authenticate user")
        print("4. Exit")
        choice = input("Choose option (1-4): ")
        if choice == '1':
            l = input("Enter login: ")
            p = input("Enter password: ")
            fn = input("Enter full name: ")
            add_user(l, p, fn)
        elif choice == '2':
            l = input("Enyer user login: ")
            p = input("Enter new password: ")
            update_user_password(l, p)
        elif choice == '3':
            l = input("Enter login: ")
            p = input("Enter password: ")
            authenticate_user(l, p)
        elif choice == '4':
            print("bye")
            break
        else:
            print("Wrong choice, please try again.")