from datetime import datetime

class ActivityLog:
    def __init__(self, activity_type, duration, calories_burned, timestamp):
        self.activity_type = activity_type
        self.duration = duration
        self.calories_burned = calories_burned
        self.timestamp = timestamp
        self.next = None

activity_head = None

def calculate_calories(activity_type, duration, weight):
    MET_VALUES = {
        "Running": 9.8,
        "Cycling": 8.0,
        "Swimming": 6.0,
        "Walking": 3.8,
    }
    met = MET_VALUES.get(activity_type, 5.0)
    return met * weight * (duration / 60)

def log_activity(activity_type, duration, weight, timestamp=None):
    global activity_head
    # If no timestamp is provided, set it to the current time
    if timestamp is None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    calories = calculate_calories(activity_type, duration, weight)
    new_log = ActivityLog(activity_type, duration, calories, timestamp)
    
    if not activity_head:
        activity_head = new_log
    else:
        current = activity_head
        while current.next:
            current = current.next
        current.next = new_log

    return f"Activity logged: {activity_type}, {calories:.2f} kcal burned."

def display_activity_history():
    global activity_head
    activities = []
    current = activity_head
    while current:
        activities.append(
            f"{current.timestamp} - {current.activity_type}: {current.duration} min, {current.calories_burned:.2f} kcal"
        )
        current = current.next
    return "\n".join(activities) if activities else "No activities logged yet."
