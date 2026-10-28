users = {
    "alice": "admin",
    "bob": "user"
}
def login(username):
    if username in users:
        role = users[username]
        print(f"Login successful: {username} ({role})")
        return role
    else:
        print("Login failed: User not found.")
        return None

def admin_action(role):
    if role == "admin":
        print("Access granted: Admin dashboard.")
    else:
        print("Access denied: Admins only.")

def user_action(role):
    if role == "user":
        print("Access granted: User dashboard.")
    else:
        print("Access denied: Regular users only.")


print("--- Admin Login ---")
admin_role = login("alice")
admin_action(admin_role)
user_action(admin_role)

print("\n--- Regular User Login ---")
user_role = login("bob")
admin_action(user_role)
user_action(user_role)


## This app demonstrates Confidentiality by restricting access based on user roles
## Only admins have access to the admin dashboard, while users are restricted to the user board.