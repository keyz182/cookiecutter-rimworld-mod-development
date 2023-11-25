import os

#About is always made
os.makedirs("{{cookiecutter.mod_ver}}/Defs", exist_ok=True)
os.makedirs("{{cookiecutter.mod_ver}}/Patches", exist_ok=True)
os.makedirs("{{cookiecutter.mod_ver}}/Assemblies", exist_ok=True)
os.makedirs("Common/Languages", exist_ok=True)
os.makedirs("Common/Sounds", exist_ok=True)
os.makedirs("Common/Textures", exist_ok=True)
