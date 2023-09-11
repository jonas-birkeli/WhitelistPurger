import sys
import requests
import json
from datetime import datetime


whitelist_filename = 'whitelist.json'
whitelist_dated_filename = 'whitelist_dated.json'
current_time = datetime.now().today()


def main():
	global uuid
	if not len(sys.argv) == 2:
		print('Error parsing commandline argument')
		print('Usage: python whitelist_add.py username')
		sys.exit(1)

	username = sys.argv[1]

	response = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{username}')
	if response.status_code == 200:
		data = response.json()
		uuid = data.get('id')

	new_data = {
		'uuid': uuid,
		'name': username
	}
	new_data_dated = {
		'uuid': uuid,
		'name': username,
		'date': str(current_time)
	}

	try:
		with open(whitelist_filename, 'r') as f:
			existing_data = json.load(f)
	except (FileNotFoundError, json.JSONDecodeError):
		existing_data = []  # File not found, empty list

	if new_data in existing_data:  # Duplicate check
		print('User already in whitelist.')
		sys.exit(1)

	existing_data.append(new_data)

	try:
		with open(whitelist_dated_filename, 'r') as f:
			existing_dated_data = json.load(f)
	except (FileNotFoundError, json.JSONDecodeError):
		existing_dated_data = []  # File not found, empty list

	existing_dated_data.append(new_data_dated)

	with open(whitelist_filename, 'w') as f:
		json.dump(existing_data, f, indent=2)

	with open(whitelist_dated_filename, 'w') as f:
		json.dump(existing_dated_data, f, indent=2)

	print(f'Successfully added {new_data} to whitelist')


if __name__ == '__main__':
	main()
	sys.exit()
