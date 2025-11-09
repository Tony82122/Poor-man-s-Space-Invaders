@echo off
REM Poor Man's Space Invaders - Windows Launcher
echo ========================================
echo   Poor Man's Space Invaders
echo   Starting game...
echo ========================================
echo.

cd /d "%~dp0\Alien_Invasion"

REM Check if pygame is installed
python -c "import pygame" 2>nul
if errorlevel 1 (
    echo Pygame not found! Installing...
    pip install pygame
    if errorlevel 1 (
        echo Error: Could not install pygame
        echo Please run: pip install pygame
        pause
        exit /b 1
    )
)

echo Launching game...
python Alien_Invasion.py

if errorlevel 1 (
    echo.
    echo Error: Game encountered an error
    pause
)
