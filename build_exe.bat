@echo off
REM ----------------------------------------------
REM Batch script to build Cyberpunk Countdown Timer as an .exe
REM ----------------------------------------------

REM Navigate to the script's directory
cd /d "%~dp0"

REM Activate the virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat
if %errorlevel% neq 0 (
    echo Failed to activate virtual environment.
    pause
    exit /b 1
)

REM Upgrade pip to the latest version
echo Upgrading pip...
python -m pip install --upgrade pip
if %errorlevel% neq 0 (
    echo Failed to upgrade pip.
    pause
    exit /b 1
)

REM Install or upgrade dependencies
echo Installing dependencies from requirements.txt...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Failed to install dependencies.
    pause
    exit /b 1
)

REM Install PyInstaller if not already installed
echo Installing PyInstaller...
pip install --upgrade pyinstaller
if %errorlevel% neq 0 (
    echo Failed to install PyInstaller.
    pause
    exit /b 1
)

REM Clean previous build (optional)
echo Cleaning previous build...
if exist build (
    rmdir /s /q build
)
if exist dist (
    rmdir /s /q dist
)
if exist __pycache__ (
    rmdir /s /q __pycache__
)
if exist metronome.spec (
    del metronome.spec
)

REM Build the executable using PyInstaller
echo Building the executable with PyInstaller...
pyinstaller --onefile --windowed ^
    --icon "assets\images\Icon.ico" ^
    --add-data "assets\images;assets\images" ^
    --add-data "assets\sounds;assets\sounds" ^
    metronome.py

if %errorlevel% neq 0 (
    echo PyInstaller encountered an error.
    pause
    exit /b 1
)

REM Deactivate the virtual environment
echo Deactivating virtual environment...
call deactivate

REM Inform the user of completion
echo.
echo Build complete! You can find the executable in the 'dist' folder.
echo.
pause
