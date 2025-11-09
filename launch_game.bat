@echo off
REM Poor Man's Space Invaders - Windows Launcher
echo ========================================
echo   Poor Man's Space Invaders
echo   Starting game...
echo ========================================
echo.

REM Use the virtual environment Python
set PYTHON_PATH=%~dp0.venv\Scripts\python.exe

REM Check if virtual environment exists
if not exist "%PYTHON_PATH%" (
    echo Virtual environment not found!
    echo Using system Python instead...
    set PYTHON_PATH=python
)

cd /d "%~dp0Alien_Invasion"

echo Launching game...
"%PYTHON_PATH%" Alien_Invasion.py

if errorlevel 1 (
    echo.
    echo Error: Game encountered an error
    echo.
    echo Make sure pygame is installed:
    echo   pip install pygame
    echo.
    pause
)
