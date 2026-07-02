# Slack Daily Planner Bot

A simple Slack bot that posts a daily planner message every weekday morning.

## What it does

The bot posts a morning planner in Slack with:
- Main focus
- Tasks
- Meetings
- Reminders
- Blockers
- End-of-day updates

## Schedule

Runs Monday to Friday at 8 AM Pacific during PDT.

Cron:
0 15 * * 1-5

## How to use

When the planner message appears in Slack, team members can reply with:
- What they are working on
- Any blockers
- Meeting notes or reminders
- End-of-day progress updates

## Setup needed

The GitHub repo needs this secret:
SLACK_WEBHOOK_URL

This stores the Slack webhook URL securely.
