import os
import json
import requests
import gspread
from datetime import datetime

SLACK_WEBHOOK_URL = os.environ["SLACK_WEBHOOK_URL"]
GOOGLE_SHEET_ID = os.environ["GOOGLE_SHEET_ID"]
GOOGLE_SERVICE_ACCOUNT_JSON = os.environ["GOOGLE_SERVICE_ACCOUNT_JSON"]


def get_latest_form_response():
    service_account_info = json.loads(GOOGLE_SERVICE_ACCOUNT_JSON)

    client = gspread.service_account_from_dict(service_account_info)
    sheet = client.open_by_key(GOOGLE_SHEET_ID).sheet1

    rows = sheet.get_all_records()

    if not rows:
        return None

    return rows[-1]


def build_summary_message():
    today = datetime.now().strftime("%A, %B %d, %Y")
    response = get_latest_form_response()

    if not response:
        text = f"""*Daily Planner — {today}*

No planner response has been submitted yet.
"""
        return {"text": text}

    lines = [f"*Daily Planner — {today}*", ""]

    for key, value in response.items():
        if value:
            lines.append(f"*{key}:*")
            lines.append(str(value))
            lines.append("")

    return {"text": "\n".join(lines)}


def post_to_slack():
    message = build_summary_message()
    response = requests.post(SLACK_WEBHOOK_URL, json=message, timeout=10)
    response.raise_for_status()
    print("Daily Planner summary posted to Slack.")


if __name__ == "__main__":
    post_to_slack()
