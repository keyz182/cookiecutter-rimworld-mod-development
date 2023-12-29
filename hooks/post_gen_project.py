import os
import shutil
import subprocess

#About is always made
os.makedirs("{{cookiecutter.mod_ver}}/Defs", exist_ok=True)
os.makedirs("{{cookiecutter.mod_ver}}/Patches", exist_ok=True)
os.makedirs("{{cookiecutter.mod_ver}}/Assemblies", exist_ok=True)
os.makedirs("Common/Languages", exist_ok=True)
os.makedirs("Common/Sounds", exist_ok=True)
os.makedirs("Common/Textures", exist_ok=True)

# Check if git binary is available
git_path = shutil.which('git')
if git_path is not None:
    # Initialize a Git repository in the current directory
    subprocess.run(['git', 'init'])
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', 'Cookie cutter initial commit'])
else:
    print("Git binary not found. Skipping git initialisation.")
