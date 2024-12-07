import matplotlib.pyplot as plt
from io import BytesIO

# Progress tracking data structure (this can be any other structure based on your needs)
progress_tree = {}

# Insert progress for an activity
def insert_progress(progress_tree, activity_type, calories_burned):
    # Update progress in your data structure (you could replace this with any logic you want)
    if activity_type not in progress_tree:
        progress_tree[activity_type] = calories_burned
    else:
        progress_tree[activity_type] += calories_burned
    return progress_tree

# Function to view progress and generate a pie chart
def view_progress():
    # Example logic to calculate progress toward a goal
    total_calories_burned = sum(progress_tree.values())
    target_calories = 5000  # Assuming a target goal of 5000 calories for simplicity

    progress = total_calories_burned
    remaining = target_calories - progress

    # Pie chart for progress visualization
    labels = ['Progress', 'Remaining']
    sizes = [progress, remaining]
    colors = ['#4CAF50', '#FFC107']

    # Create figure for pie chart
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title("Goal Progress Tracker")

    # Save the plot to a BytesIO object so Gradio can display it as an image
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)  # Rewind the buffer to the beginning
    img = buf.read()  # Read the image into memory

    return img  # Return the image as the output
