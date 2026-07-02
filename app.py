import os
import json
import requests
from datetime import datetime

SLACK_WEBHOOK_URL = os.environ["SLACK_WEBHOOK_URL"]
PLANNER_FILE = "planner.json"


def load_planner():
    with open(PLANNER_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def format_list(items):
    if not items:
        return "- None"
    return "\n".join(f"- {item}" for item in items)


def build_message():
    planner = load_planner()
    today = datetime.now().strftime("%A, %B %d, %Y")

    text = f"""Good morning team :sunny:

*Daily Planner — {today}*

*Main focus:*
{format_list(planner.get("main_focus", []))}

*Tasks:*
{format_list(planner.get("tasks", []))}

*Meetings:*
{format_list(planner.get("meetings", []))}

*Reminders:*
{format_list(planner.get("reminders", []))}

*Blockers to raise:*
{format_list(planner.get("blockers", []))}

*End-of-day update due:*
{format_list(planner.get("end_of_day_update", []))}
"""

    return {"text": text}


def post_to_slack():
    message = build_message()
    response = requests.post(SLACK_WEBHOOK_URL, json=message, timeout=10)
    response.raise_for_status()
    print("Daily planner posted to Slack.")


if __name__ == "__main__":
    post_to_slack()
