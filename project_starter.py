# this script sets clones a git repo
# sets up env environment
# upgrades pip
# installs flake8

import subprocess
import pathlib

# input
git_repo = "https://github.com/jeffcall-ch/test"
proxy = " -- proxy https://148.64.11.164:8080 "


git_repo_name = git_repo.split("/")[-1]
print("Git repo name is:  " + git_repo_name)

git_repo_home_folder = pathlib.Path.home() / "Python" / "Python_repos"
git_repo_folder = git_repo_home_folder / git_repo_name
env_script_folder = git_repo_folder / "env" / "Scripts"

print(git_repo_home_folder)

subprocess.call('dir', cwd=str(git_repo_home_folder), shell=True)
# subprocess.call('git clone ' + git_repo, cwd=str(git_repo_home_folder), shell=True)

subprocess.call('mkdir env', cwd=str(git_repo_folder), shell=True)

subprocess.call('./env/Scripts/Activate.ps1', cwd=str(git_repo_folder), shell=True)
subprocess.call('dir', cwd=str(git_repo_folder), shell=True)

# activate env
