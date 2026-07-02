# Slack Daily Planner Bot

Posts a daily planner message to Slack every weekday morning.

## Setup

1. Create a Slack Incoming Webhook.
2. Add the webhook URL as a GitHub secret named:

SLACK_WEBHOOK_URL

3. Push this repo to GitHub.
4. Run the workflow manually from the GitHub Actions tab to test.

## Schedule

The bot runs on this cron schedule:

0 14 * * 1-5

GitHub Actions cron uses UTC.
