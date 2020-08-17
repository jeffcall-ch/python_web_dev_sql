# this script sets clones a git repo
# sets up env environment
#   - upgrades pip
#   - installs flake8 

import subprocess
import pathlib
import platform


# input
git_repo = "https://github.com/jeffcall-ch/excel_bom_compare"
proxy = "--proxy https://148.64.11.164:8080"

# variables
git_repo_name = git_repo.split("/")[-1]
pytho_repo_home = pathlib.Path.home() / "Python" / "Python_repos"
current_repo_folder = pytho_repo_home / git_repo_name
env_folder = current_repo_folder / "env"
env_script_folder = env_folder / "Scripts"
requirements_file = current_repo_folder / "requirements.txt"
win_pip_exec = env_script_folder / "pip"
win_python_exec = env_script_folder / "python"

print(platform.system())


def main():
    create_folders()
    create_venv()
    install_packages() 

def create_folders():
    if not current_repo_folder.exists():
        subprocess.call('git clone ' + git_repo, cwd=str(pytho_repo_home), shell=True)
    if not env_folder.exists():
        subprocess.call('mkdir env', cwd=str(current_repo_folder), shell=True)

def create_venv():
    if not env_script_folder.exists():
        subprocess.call(f'python -m venv {env_folder}', cwd=str(current_repo_folder), shell=True)


def install_packages():
    # upgrade pip to latest
    subprocess.call(f'{win_pip_exec} {proxy} install --upgrade pip', cwd=str(current_repo_folder), shell=True)
    
    # install all from requirements.txt
    if requirements_file.exists():
        subprocess.call(f'{win_pip_exec} {proxy} install -r requirements.txt', cwd=str(current_repo_folder), shell=True)
    
    # install additional packages
    subprocess.call(f'{win_pip_exec} {proxy} install -U flake8', cwd=str(current_repo_folder), shell=True)


if __name__ == "__main__":
    main()
