
# OpenClaw Cron Jobs

Each cron job is defined by a schedule (cron expression) and a command to execute.

## Nighttime Futures Data

Schedule: 10 5 * * *
Command: cd /home/dm/Projects/Taifex && source venv/bin/activate && python3 run_nighttime_api_cron.py
Message: Fetching nighttime futures data...
Channel: telegram
