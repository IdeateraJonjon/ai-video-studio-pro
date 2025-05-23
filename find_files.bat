@echo off
color 0A
title AI Video Studio - File Finder
echo.
echo ╔══════════════════════════════════════════════════════════════╗
echo ║                    FILE LOCATION GUIDE                       ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.
echo 📁 ALL FILES ARE LOCATED IN: C:\AI_Video_Generation\
echo.
echo 🚀 MAIN FILES TO USE:
echo    launcher.bat           ← START HERE (Menu system)
echo    studio_launch.py       ← Server with :5000
echo    studio_production.py   ← Server without :5000 (needs Admin)
echo    setup_domain.bat       ← Setup custom domains (needs Admin)
echo.
echo 📖 DOCUMENTATION:
echo    README.md             ← Complete guide
echo    QUICK_START.md        ← 5-minute setup
echo    FILE_LOCATIONS.md     ← This guide
echo.
echo 📂 CURRENT DIRECTORY CONTENTS:
echo.
dir /b C:\AI_Video_Generation\*.bat
dir /b C:\AI_Video_Generation\*.py
dir /b C:\AI_Video_Generation\*.md
echo.
echo 🎯 QUICK ACTIONS:
echo [1] Open AI Video Generation folder
echo [2] Run main launcher
echo [3] Setup domains (Admin required)
echo [4] View complete file list
echo [5] Exit
echo.
set /p choice="Select option (1-5): "

if "%choice%"=="1" goto open_folder
if "%choice%"=="2" goto run_launcher
if "%choice%"=="3" goto setup_domains
if "%choice%"=="4" goto show_files
if "%choice%"=="5" goto exit

:open_folder
explorer C:\AI_Video_Generation\
echo Opened AI Video Generation folder!
goto menu

:run_launcher
cd /d C:\AI_Video_Generation
call launcher.bat
goto menu

:setup_domains
echo.
echo IMPORTANT: This requires Administrator privileges!
echo Right-click Command Prompt and "Run as administrator"
pause
cd /d C:\AI_Video_Generation
call setup_domain.bat
goto menu

:show_files
echo.
echo COMPLETE FILE LIST:
echo ==================
dir C:\AI_Video_Generation\
echo.
echo SUBDIRECTORIES:
echo ===============
dir C:\AI_Video_Generation\ /ad
goto menu

:exit
echo.
echo All files are in: C:\AI_Video_Generation\
echo Start with: launcher.bat
pause
exit

:menu
echo.
echo Press any key to return to menu...
pause >nul
cls
goto start

:start
goto menu
