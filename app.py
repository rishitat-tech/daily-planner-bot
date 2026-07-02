import os
import requests
from datetime import datetime

SLACK_WEBHOOK_URL = os.environ["SLACK_WEBHOOK_URL"]

PLANNER_FORM_URL = "https://github.com/rishitat-tech/daily-planner-bot/issues/new?template=daily_planner.yml"


def build_message():
    today = datetime.now().strftime("%A, %B %d, %Y")

    text = f"""Good morning team :sunny:

*Daily Planner — {today}*

Please fill out today's planner form:

{PLANNER_FORM_URL}

The form is for:
- Main focus
- Tasks
- Meetings
- Blockers
- End-of-day update
"""

    return {"text": text}


def post_to_slack():
    message = build_message()
    response = requests.post(SLACK_WEBHOOK_URL, json=message, timeout=10)
    response.raise_for_status()
    print("Daily planner form reminder posted to Slack.")


if __name__ == "__main__":
    post_to_slack()
