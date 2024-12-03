import sqlite3

# Function to connect to the SQLite database
def connect_db():
    conn = sqlite3.connect("databases/users.db")
    cursor = conn.cursor()
    return conn, cursor

# Function to add a new user to the database
def add_user(name, email, password, age, gender, weight):
    conn, cursor = connect_db()
    try:
        cursor.execute('''
        INSERT INTO users (name, email, password, age, gender, weight)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (name, email, password, age, gender, weight))
        conn.commit()
        print(f"User {name} added successfully!")
    except sqlite3.IntegrityError:
        print("Error: Email already exists.")
    finally:
        conn.close()

# Function to view user details based on email
def view_user(email):
    conn, cursor = connect_db()
    cursor.execute('''
    SELECT * FROM users WHERE email = ?
    ''', (email,))
    user = cursor.fetchone()
    conn.close()
    
    if user:
        print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}, Age: {user[4]}, Gender: {user[5]}, Weight: {user[6]}")
    else:
        print("User not found.")

# Function to update user's weight
def update_weight(email, new_weight):
    conn, cursor = connect_db()
    cursor.execute('''
    UPDATE users
    SET weight = ?
    WHERE email = ?
    ''', (new_weight, email))
    conn.commit()
    conn.close()
    print(f"Weight for user with email {email} updated to {new_weight}.")

# Function to get all users (use a cache to implement DSA concepts)
def get_all_users():
    conn, cursor = connect_db()
    cursor.execute('''
    SELECT * FROM users
    ''')
    users = cursor.fetchall()
    conn.close()

    # Store users in a cache (dictionary) to simulate efficient searching (O(1) for lookup)
    user_cache = {user[2]: user for user in users}  # Using email as key (email is unique)
    
    return user_cache

# Function to search for a user using Linear Search (as an example of DSA)
def search_user_by_email(email):
    user_cache = get_all_users()  # Fetch users from database and store in cache
    # Linear Search through the user_cache dictionary by email
    if email in user_cache:
        user = user_cache[email]
        print(f"User found: ID: {user[0]}, Name: {user[1]}, Email: {user[2]}, Age: {user[4]}, Gender: {user[5]}, Weight: {user[6]}")
    else:
        print("User not found.")

# Example Usage
# if __name__ == "__main__":
    # Add users
    # add_user("Test User Two", "testusertwo@example.com", "password123two", 27, "Female", 72)
    
    # View user
    # view_user("testusertwo@example.com")
    
    # Update weight
    # update_weight("testusertwo@example.com", 185)
    
    # # Search user by email (using Linear Search from cache)
    # search_user_by_email("alice@example.com")
