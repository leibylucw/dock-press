import subprocess


def exportPlugins():
	command = 'docker compose cp wordpress:/var/www/html/wp-content/plugins ./wp-content'

	try:
		result = subprocess.run(command, check=True, capture_output=True, text=True)
	except subprocess.CalledProcessUrlError as e:
		print(f"Command '{e.cmd}' returned non-zero exit status {e.returncode}")
		print(f'Error output: {e.stderr}')
		raise


def main():
	print('Exporting plugins...', end='', flush=True)
	exportPlugins()
	print('Done')


if __name__ == '__main__':
	main()
