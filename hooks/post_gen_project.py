import os

#About is always made
os.makedirs("{{cookiecutter.mod_name}}/{{cookiecutter.mod_ver}}/Defs", exist_ok=True)
os.makedirs("{{cookiecutter.mod_name}}/{{cookiecutter.mod_ver}}/Patches", exist_ok=True)
os.makedirs("{{cookiecutter.mod_name}}/Common/Languages", exist_ok=True)
os.makedirs("{{cookiecutter.mod_name}}/Common/Sounds", exist_ok=True)
os.makedirs("{{cookiecutter.mod_name}}/Common/Textures", exist_ok=True)
