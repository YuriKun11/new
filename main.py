import os
import subprocess

def run_command(command):
    """Run a command in the shell and print the output."""
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode == 0:
        print(stdout.decode())
    else:
        print(stderr.decode())

run_command('git init')

run_command('git add .')

run_command('git status')

email = input("Enter your Gmail address: ")
run_command(f'git config --global user.email "{email}"')

run_command('git commit -m "First commit"')

repo_link = input("Enter the repository link: ")
run_command(f'git remote add origin {repo_link}')

run_command('git push -u origin master')


# -------If you want to push codes on different repository-------
# git remote remove origin
# git remote add origin {https://github.com/user/new}
# git push -u origin master

# -------If you want to change the content of your repo-------
# git pull origin master
# git add .
# git commit -m "Resolved merge conflicts"

# git push -u origin master

# remove connections 
# rmdir /s /q .git


# reinitialize git after removing connection
# git pull origin master --allow-unrelated-histories
# git add . 
# git commit -m "Resolved merge conflicts and merged unrelated histories"
# git push origin master
