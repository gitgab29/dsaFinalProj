import gradio as gr
from user_profile import add_user
from activity_log import log_activity, display_activity_history
from progress_tracker import view_progress
from recommendations import get_recommendation
from datetime import datetime
from io import BytesIO
import matplotlib.pyplot as plt

# Create the UI for logging activities
def log_activity_ui(activity_type, duration, weight):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    calories = log_activity(activity_type, duration, weight, timestamp)
    return calories, display_activity_history()

# Create the UI for viewing progress
def progress_tracker_ui():
    return view_progress()

# Create the UI for recommendations
def recommendation_ui(goal):
    return get_recommendation(goal)

# Define the dropdowns and input elements for the interface
with gr.Blocks() as app:
    # Apply a color scheme and some layout customizations
    with gr.Column(elem_id="profile", scale=1):
        with gr.Tab("Create Profile"):
            gr.Markdown(
                """<h1 style="text-align: center; color: #4CAF50;">Welcome to Your Fitness Tracker</h1>""",
                elem_id="header"
            )
            with gr.Row():
                name = gr.Textbox(label="Name", placeholder="Enter your name", elem_id="name_field")
                height = gr.Number(label="Height (cm)", elem_id="height_field")
                weight = gr.Number(label="Weight (kg)", elem_id="weight_field")
            goal = gr.Dropdown(choices=["Lose Weight", "Gain Weight", "Better Cardio"], label="Goal", elem_id="goal_dropdown")
            submit_profile = gr.Button("Add Profile", elem_id="submit_profile")
            profile_status = gr.Textbox(label="Profile Status", interactive=False, elem_id="profile_status")
            submit_profile.click(add_user, inputs=[name, height, weight, goal], outputs=profile_status)
    
    with gr.Tab("Log Activity"):
        with gr.Row():
            activity_type = gr.Dropdown(choices=["Running", "Cycling", "Swimming", "Walking"], label="Activity Type", elem_id="activity_dropdown")
            duration = gr.Number(label="Duration (minutes)", elem_id="duration_field")
            weight_input = gr.Number(label="Weight (kg)", elem_id="weight_input_field")
        submit_activity = gr.Button("Log Activity", elem_id="submit_activity")
        calories_burned = gr.Textbox(label="Calories Burned", interactive=False, elem_id="calories_burned")
        activity_history = gr.Textbox(label="Activity History", interactive=False, elem_id="activity_history")
        submit_activity.click(log_activity_ui, inputs=[activity_type, duration, weight_input], outputs=[calories_burned, activity_history])

    with gr.Tab("Progress Tracker"):
        progress_button = gr.Button("View Progress", elem_id="view_progress_button")
        progress = gr.Image(label="Progress", interactive=False, elem_id="progress_img")
        progress_button.click(progress_tracker_ui, outputs=progress)

    with gr.Tab("Recommendations"):
        goal_input = gr.Dropdown(choices=["Lose Weight", "Gain Weight", "Better Cardio"], label="Goal", elem_id="goal_recommendations_dropdown")
        get_recommendations_button = gr.Button("Get Recommendations", elem_id="get_recommendations_button")
        recommendations = gr.Textbox(label="Recommendations", interactive=False, elem_id="recommendations_output")
        get_recommendations_button.click(recommendation_ui, inputs=[goal_input], outputs=recommendations)

# Custom CSS to improve the UI appearance
app.css = """
    #profile {background-color: #f0f8ff; padding: 20px;}
    #submit_profile {background-color: #4CAF50; color: white; font-size: 16px;}
    #submit_activity {background-color: #FFC107; color: white; font-size: 16px;}
    #view_progress_button {background-color: #4CAF50; color: white; font-size: 16px;}
    #get_recommendations_button {background-color: #FFC107; color: white; font-size: 16px;}
    #header {font-size: 24px; font-weight: bold; color: #4CAF50;}
    .gradio-row {margin-bottom: 20px;}
    .gradio-input {padding: 10px; font-size: 14px; border-radius: 5px;}
    .gradio-textbox {border-radius: 5px; padding: 10px; font-size: 14px;}
    #activity_history {height: 200px; overflow-y: scroll; background-color: #f1f1f1;}
    #profile_status {background-color: #e8f5e9;}
"""

# Launch the app
app.launch(share=True)
