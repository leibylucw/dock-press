import argparse
import os
import subprocess

DUMP_FILE = 'db'
DUMP_FILE_EXTENSION = '.sql'
DUMP_FILE_NAME = f'{DUMP_FILE}{DUMP_FILE_EXTENSION}'
EXPORT_DIRECTORY = 'exported_assets'
WORDPRESS_DIRECTORY = '/var/www/html/wp-content'


def exportDatabase():
	print('Exporting database...', end='', flush=True)

	createDBDumpCommand = f'docker compose exec -it mysql bash -c "mysqldump -p$MYSQL_ROOT_PASSWORD --databases $MYSQL_DATABASE > {DUMP_FILE_NAME}"'
	copyDBDumpCommand = f'docker compose cp mysql:/{DUMP_FILE_NAME} ./{EXPORT_DIRECTORY}'

	runCommands([createDBDumpCommand, copyDBDumpCommand])

	print('Done')


def exportPlugins():
	print('Exporting plugins...', end='', flush=True)

	copyPluginsCommand = f'docker compose cp wordpress:{WORDPRESS_DIRECTORY}/plugins ./{EXPORT_DIRECTORY}'

	runCommands([copyPluginsCommand])

	print('Done')


def exportUploads():
	print('Exporting uploads...', end='', flush=True)

	copyUploadsCommand = f'docker compose cp wordpress:{WORDPRESS_DIRECTORY}/uploads ./{EXPORT_DIRECTORY}'

	runCommands([copyUploadsCommand])

	print('Done')


def makeExportDirectory():
	if not os.path.exists(EXPORT_DIRECTORY):
		os.makedirs(EXPORT_DIRECTORY)


def runCommands(commands):
	if not isinstance(commands, list):
		raise TypeError(f'commands is of type {type(commands)}, must be list')

	for command in commands:
		try:
			result = subprocess.run(command, check=True, capture_output=True, text=True)
		except subprocess.CalledProcessError as e:
			print(f"\nCommand '{e.cmd}' returned non-zero exit status {e.returncode}")
			print(f'Error output: {e.stderr}')
			raise


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

	makeExportDirectory()

	if args.database:
		exportDatabase()
	if args.plugins:
		exportPlugins()
	if args.uploads:
		exportUploads()


if __name__ == '__main__':
	main()
