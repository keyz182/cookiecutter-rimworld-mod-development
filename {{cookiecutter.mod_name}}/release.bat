@ECHO OFF
ECHO Building {{cookiecutter.mod_name}} {{cookiecutter.mod_ver}} - Started
@ECHO ON
dotnet restore {{cookiecutter.mod_name}}/{{cookiecutter.mod_ver}}/Source/{{cookiecutter.mod_name.replace(' ', '_')}}.sln
dotnet build {{cookiecutter.mod_name}}/{{cookiecutter.mod_ver}}/Source/{{cookiecutter.mod_name.replace(' ', '_')}}.sln /p:Configuration=Release
@ECHO OFF
ECHO Building {{cookiecutter.mod_name}} {{cookiecutter.mod_ver}} - Complete
ECHO Press any key to exit...
PAUSE > NUL
