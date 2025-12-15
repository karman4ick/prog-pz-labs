import hashlib
import datetime
class User:
    def __init__(self,username: str,password:str,is_active: bool=True):
        self.username = username
        self.password_hash = self._hash_password(password)
        self.is_active = is_active
    def _hash_password(self,password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()
    def verify_password(self,password: str) -> bool:
        return self.password_hash == self._hash_password(password)
class Administrator(User):
    def __init__(self, username: str, password: str, permissions=None):
        super().__init__(username, password)
        self.permissions = permissions if permissions else []
    def add_permission(self, permission: str):
        self.permissions.append(permission)
class RegularUser(User):
    def __init__(self, username: str, password: str):
        super().__init__(username, password)
        self.last_login = None
    def update_last_login(self):
        self.last_login = datetime.datetime.now
class GuestUser(User):
    def __init__(self, username: str):
        super().__init__(username,password="",is_active=True)
        self.is_guest = True
class AccessControl:
    def __init__(self):
        self.users = {}
    def add_user(self, user: User):
        self.users[user.username] = user
    def authenticate_user(self, username: str, password: str):
        user = self.users.get(username)
        if user is None:
            return None
        if not user.is_active:
            return None
        if user.verify_password(password):
            return user
        return None

ac = AccessControl()
admin = Administrator("admin", "admin123", permissions=["manage_users", "edit_settings"])
user = RegularUser("karma", "password123")
guest = GuestUser("guest")
ac.add_user(admin)
ac.add_user(user)
ac.add_user(guest)
authenticated_user = ac.authenticate_user("karma", "password123")
if authenticated_user:
    print(f"User {authenticated_user.username} logged in successfully")
else:
    print("Authentication failed")