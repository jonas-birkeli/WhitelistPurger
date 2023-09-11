# WhitelistPurger

Spigot API plugin for keeping whitelists fresh

Use whitelist_app.py to add users to whitelist
User whitelist_purge.py to freshen up the whitelist. Edit "month_target" to specify months

Schedule purger daily using crontab:

$ crontab -e

$ 0 0 * * * /usr/bin/python /path/to/script/whitelist_purge.py
