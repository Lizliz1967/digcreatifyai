# templates/ - Customizable Templates & AI Recommendation Logic for DigCreatifyAI

import random
import json

# Predefined Template Structures
templates = {
    "ebook": {
        "title": "Your eBook Title",
        "chapters": [
            {"title": "Introduction", "content": "Write about the introduction here..."},
            {"title": "Chapter 1", "content": "Main content goes here..."},
            {"title": "Conclusion", "content": "Summarize key points..."}
        ]
    },
    "printable": {
        "title": "Custom Printable",
        "sections": [
            {"header": "Planner Title", "content": "Daily tasks and schedule."},
            {"header": "Notes", "content": "Write your notes here..."}
        ]
    },
    "design_template": {
        "type": "Business Card",
        "elements": {
            "name": "Your Name",
            "contact": "your.email@example.com",
            "style": "Modern"
        }
    }
}

# AI-Driven Content Recommendation
def recommend_template(user_preferences):
    """Recommends a suitable template based on user input."""
    if user_preferences.get("category") == "ebook":
        return templates["ebook"]
    elif user_preferences.get("category") == "printable":
        return templates["printable"]
    elif user_preferences.get("category") == "design_template":
        return templates["design_template"]
    else:
        return random.choice(list(templates.values()))

# Example Usage
if __name__ == "__main__":
    user_pref = {"category": "ebook"}
    selected_template = recommend_template(user_pref)
    print(json.dumps(selected_template, indent=4))

