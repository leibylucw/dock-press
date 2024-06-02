# Python Scripts
dock-press comes with a suite of Python scripts that automate various operations you'd otherwise have to perform with Docker directly.

## Requirements
Please ensure you have read the [repository's README](../README.md) before proceeding.

### Install System Dependencies
* [CPython](https://www.python.org/): version 3.6 or higher.
* [pipx](https://github.com/pypa/pipx): version 1.4.3 or higher.  Use the `ensurepath` subcommand as described in the installation documentation to make sure you can run `pipx` from anywhere.

### Install pre-commit
dock-press uses [pre-commit](https://pre-commit.com/) for managing Git hooks. Install it with:

```shell
pipx install pre-commit
```

NOTE: You must install pre-commit regardless if you are developing new or existing Python scripts.

### Install the pre-commit Hooks
See the dev notes section for more info about pre-commit hooks. For now, all you need to do is install them using the following command:

```shell
pre-commit install
```

### **SKIP THIS SECTION
This section originally instructed users to set up a virtualenv, but it currently is not needed.

#### Create a Virtual Environment (virtualenv)
A virtual environment (virtualenv) must be used when running or developing these scripts. All subsequent sections assume that you have created the virtualenv and activated it. To create it, run the following command:

```shell
python -m venv .venv
```

#### Activate the Virtualenv
For Command Prompt on Windows:

```cmd
.\.venv\Scripts\activate.bat
```

For PowerShell on Windows:

```powershell
.\.venv\Scripts\activate.ps1
```

For Linux/MacOS:

```sh
source .venv/bin/activate
```

To deactivate the virtualenv on all platforms:

```shell
deactivate
```

#### Install Script Requirements
These scripts requires certain dependencies to be installed. To install them, run the following commands:

```shell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## General Development Notes
You will notice from the various configuration files in the repo that there are several tools to ensure certain code hygiene and quality conventions are enforced. You may wish to become familiar with these tools and the coding style configurations therein. For more info, please refer to:
* [Ruff](https://github.com/astral-sh/ruff): used for code linting and formatting
* [pre-commit](https://github.com/pre-commit/pre-commit): used for managing pre-commit hooks
