@ECHO OFF
ECHO Building {{cookiecutter.mod_name}} {{cookiecutter.mod_ver}} - Started

dotnet --list-sdks | findstr /R /C:"8\..*" 1>nul
if %errorlevel% neq 0 (
    ECHO .NET 8 SDK not found. Please install it using the following command:
    ECHO winget install Microsoft.DotNet.SDK.8
    PAUSE > NUL
    EXIT /B
)

@ECHO ON
dotnet restore {{cookiecutter.mod_ver}}/Source/{{cookiecutter.mod_name.replace(' ', '_')}}.sln
dotnet build {{cookiecutter.mod_ver}}/Source/{{cookiecutter.mod_name.replace(' ', '_')}}.sln /p:Configuration=Release
@ECHO OFF
ECHO Building {{cookiecutter.mod_name}} {{cookiecutter.mod_ver}} - Complete
ECHO Press any key to exit...
PAUSE > NUL
