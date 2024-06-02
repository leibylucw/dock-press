import argparse
import os
import subprocess

import dotenv

DUMP_FILE = 'db'
DUMP_FILE_EXTENSION = '.sql'
DUMP_FILE_ENCODING = 'utf-8'
ENVIRONMENT_VARIABLE_FILE_NAME = 'mysql.env'
ENVIRONMENT_VARIABLE_FILE_PATH = os.path.join(os.path.dirname(__file__), ENVIRONMENT_VARIABLE_FILE_NAME)
dotenv.load_dotenv(dotenv_path=ENVIRONMENT_VARIABLE_FILE_PATH)


def exportDatabase():
	command = f'docker compose exec -it mysql bash -c "mysqldump -p{os.getenv('MYSQL_ROOT_PASSWORD')} --databases {os.getenv('MYSQL_DATABASE')}"'
	with open(f'{DUMP_FILE}{DUMP_FILE_EXTENSION}', 'w', encoding=DUMP_FILE_ENCODING) as file:
		result = subprocess.run(command, stdout=file, text=True)


def exportPlugins():
	print('Exporting plugins...', end='', flush=True)

	command = 'docker compose cp wordpress:/var/www/html/wp-content/plugins ./wp-content'

	try:
		result = subprocess.run(command, check=True, capture_output=True, text=True)
	except subprocess.CalledProcessError as e:
		print(f"\nCommand '{e.cmd}' returned non-zero exit status {e.returncode}")
		print(f'Error output: {e.stderr}')
		raise

	print('Done')


def exportUploads():
	print('Exporting uploads...', end='', flush=True)

	command = 'docker compose cp wordpress:/var/www/html/wp-content/uploads ./wp-content'

	try:
		result = subprocess.run(command, check=True, capture_output=True, text=True)
	except subprocess.CalledProcessError as e:
		print(f"\nCommand '{e.cmd}' returned non-zero exit status {e.returncode}")
		print(f'Error output: {e.stderr}')
		raise

	print('Done')


def buildArgs():
	parser = argparse.ArgumentParser()

	parser.add_argument(
		'-d', '--database', dest='database', action='store_true', help='If the database should be dumped'
	)
	parser.add_argument('-p', '--plugins', dest='plugins', action='store_true', help='If plugins should be exported')
	parser.add_argument('-u', '--uploads', dest='uploads', action='store_true', help='If uploads should be exported')

	args = parser.parse_args()
	return args


def main():
	args = buildArgs()

	if args.database:
		exportDatabase()
	if args.plugins:
		exportPlugins()
	if args.uploads:
		exportUploads()


if __name__ == '__main__':
	main()
