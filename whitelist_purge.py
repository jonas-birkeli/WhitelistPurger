import sys
import json
from datetime import datetime, timedelta

# ****************************
# * Months inactive to purge *
# ****************************
month_target = 2
# 12 to make it a year

whitelist_filename = 'whitelist.json'
whitelist_dated_filename = 'whitelist_dated.json'
current_date = datetime.now()


def remove_user_from_whitelist(uuid: str, username: str):
	print("Called")
	obj = {
		'uuid': uuid,
		'name': username
	}
	print(obj)

	try:
		with open(whitelist_filename, 'r') as f:
			file_content = json.load(f)
	except (FileNotFoundError, json.JSONDecodeError):
		print('Whitelist file not found')

	file_content.remove(obj)

	with open(whitelist_filename, 'w') as f:
		json.dump(file_content, f, indent=2)


def main():
	try:
		with open(whitelist_dated_filename, 'r') as f:
			file_content = json.load(f)
	except (FileNotFoundError, json.JSONDecodeError) as e:
		print(e)
		print('Dated whitelist-file not found. Exiting')
		sys.exit(1)

	pending_removal = []

	for user in file_content:
		date_string = user['date'].split()[0]
		date_object = datetime.strptime(date_string, '%Y-%m-%d')

		year_diff = current_date.year - date_object.year
		month_diff = current_date.month - date_object.month

		total_months_ago = year_diff * 12 + month_diff

		if total_months_ago >= month_target:
			remove_user_from_whitelist(user['uuid'], user['name'])
			print(f'Removed user {user["name"]} from whitelist')
			pending_removal.append(user)

	for user in pending_removal:
		file_content.remove(user)

	with open(whitelist_dated_filename, 'w') as f:
		json.dump(file_content, f, indent=2)

	print(f'Successfully purgeed {len(pending_removal)} users')


if __name__ == '__main__':
	main()
	sys.exit()
