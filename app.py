import os
import requests
from datetime import datetime

SLACK_WEBHOOK_URL = os.environ["SLACK_WEBHOOK_URL"]


def build_message():
    today = datetime.now().strftime("%A, %B %d, %Y")

    return {
        "text": f"""Good morning team :sunny:

*Daily Planner — {today}*

*Main focus:*
- 

*Tasks:*
- 
- 
- 

*Meetings:*
- 

*Reminders:*
- Please share blockers early.
- Post progress updates by end of day.

*Blockers to raise:*
- 

*End-of-day update due:*
- 
"""
    }


def post_to_slack():
    message = build_message()
    response = requests.post(SLACK_WEBHOOK_URL, json=message, timeout=10)
    response.raise_for_status()
    print("Daily planner posted to Slack.")


if __name__ == "__main__":
    post_to_slack()
