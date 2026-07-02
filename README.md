# Slack Daily Planner Bot

A simple bot that posts a daily planner message to Slack every weekday morning.

## What it does

This bot sends a scheduled Slack message with:
- Main focus
- Tasks
- Meetings
- Reminders
- Blockers
- End-of-day updates

It helps the team start the day with clear priorities and gives everyone a place to reply with updates or blockers.

## What you need

Before using this bot, you need:
- A GitHub repo
- A Slack workspace
- A Slack Incoming Webhook URL
- GitHub Actions enabled
- A GitHub Actions secret named SLACK_WEBHOOK_URL

## How to clone and use it

Run:

git clone https://github.com/rishitat-tech/daily-planner-bot.git
cd daily-planner-bot

Then add the Slack webhook URL in GitHub:

Settings -> Secrets and variables -> Actions -> New repository secret

Name:
SLACK_WEBHOOK_URL

Value:
Your Slack webhook URL

Do not put the webhook URL directly in the code.

## Schedule

The bot runs Monday to Friday at 8 AM Pacific during PDT.

Cron:
0 15 * * 1-5

The schedule is set in:
.github/workflows/daily-planner.yml

## How people use it

When the bot posts in Slack, team members can reply with:
- What they are working on
- Any blockers
- Meeting notes or reminders
- End-of-day progress updates

## Main files

app.py - Bot script
requirements.txt - Python dependencies
.github/workflows/daily-planner.yml - GitHub Actions schedule
README.md - Project instructions
