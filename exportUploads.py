import subprocess


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


def main():
	exportUploads()


if __name__ == '__main__':
	main()
