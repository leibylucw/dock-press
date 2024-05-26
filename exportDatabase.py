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


def main():
	exportDatabase()


if __name__ == '__main__':
	main()
