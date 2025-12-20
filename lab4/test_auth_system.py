import pytest
from auth_system import User, Administrator, AccessControl, RegularUser, GuestUser
def test_verify_password_success():
    user = User("testuser", "securepass")
    assert user.verify_password("securepass") is True
def test_verify_password_failure():
    user = User("testuser", "securepass")
    assert user.verify_password("wrongpass") is False
def test_add_permission_to_empty_list():
    admin = Administrator("admin","adminpass")
    admin.add_permission("delete_users")
    assert "delete_users" in admin.permissions
    assert len(admin.permissions) == 1
def test_add_additional_permission_():
    admin = Administrator("admin","adminpass", permissions=["read"])
    admin.add_permission("write")
    assert "read" in admin.permissions
    assert "write" in admin.permissions
    assert len(admin.permissions) == 2
def test_authenticate_user_success():
    ac = AccessControl()
    user = RegularUser("user1", "mypassword")
    ac.add_user(user)
    auth_result = ac.authenticate_user("user1", "mypassword")
    assert auth_result == user
    assert auth_result.username == "user1"
def test_authenticate_user_wrong_password():
    ac = AccessControl()
    user = RegularUser("user1", "mypassword")
    ac.add_user(user)
    auth_result = ac.authenticate_user("user1", "wrongpass")
    assert auth_result is None
def test_authenticate_user_not_found():
    ac = AccessControl()
    auth_result = ac.authenticate_user("ghost", "anypass")
    assert auth_result is None
def test_authenticate_user_inactive():
    ac = AccessControl()
    user = User("banned_user", "pass", is_active=False)
    ac.add_user(user)
    auth_result = ac.authenticate_user("banned_user", "pass")
    assert auth_result is None
def test_regular_user_update_login():
    user = RegularUser("steve", "pass123")
    assert user.last_login is None
    user.update_last_login()
    assert user.last_login is not None
def test_guest_user_login():
    guest = GuestUser("anonymous")
    assert guest.is_guest is True
    assert guest.is_active is True
    assert guest.verify_password("") is True