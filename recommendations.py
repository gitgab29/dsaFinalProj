def get_recommendation(goal):
    if goal == "Lose Weight":
        return "Recommendation: Try running or cycling for at least 30 minutes a day."
    elif goal == "Gain Weight":
        return "Recommendation: Focus on strength training and eat a calorie surplus."
    elif goal == "Better Cardio":
        return "Recommendation: Consistent running or swimming will improve your cardio fitness."
    else:
        return "Please select a valid goal."
