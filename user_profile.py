class UserProfile:
    def __init__(self, name, height, weight, goal):
        self.name = name
        self.height = height
        self.weight = weight
        self.goal = goal

user_profiles = []

def add_user(name, height, weight, goal):
    user_profiles.append(UserProfile(name, height, weight, goal))
    return f"User {name} added successfully!"
