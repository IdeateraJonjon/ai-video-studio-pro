@echo off
title AI Video Studio Professional
color 0B
echo.
echo  ╔══════════════════════════════════════════════════════════════╗
echo  ║                AI VIDEO STUDIO PROFESSIONAL                  ║
echo  ╚══════════════════════════════════════════════════════════════╝
echo.
echo  [1] Setup Custom Domains (Run as Administrator)
echo  [2] Launch Studio (Standard - Port 5000)
echo  [3] Launch Studio (Production - Port 80, requires Admin)
echo  [4] View Documentation
echo  [5] Exit
echo.
set /p choice="Select option (1-5): "

if "%choice%"=="1" goto setup_domains
if "%choice%"=="2" goto launch_standard
if "%choice%"=="3" goto launch_production
if "%choice%"=="4" goto show_docs
if "%choice%"=="5" goto exit

:setup_domains
echo.
echo Setting up custom domains...
echo This requires Administrator privileges!
pause
call setup_domain.bat
goto menu

:launch_standard
echo.
echo Launching AI Video Studio on port 5000...
echo Access at: http://localhost:5000
echo Custom domains: http://visual-video-studio.local:5000
python studio_launch.py
goto menu

:launch_production
echo.
echo Launching AI Video Studio on port 80 (no port number needed)...
echo Access at: http://visual-video-studio.local
python studio_production.py
goto menu

:show_docs
echo.
echo Available Documentation:
echo - README.md (Complete guide)
echo - QUICK_START.md (5-minute setup)
echo - docs\GITHUB_GUIDE.md (GitHub integration)
echo - docs\API_INTEGRATION.md (API setup)
echo.
echo Opening README.md...
start README.md
goto menu

:exit
echo.
echo Thank you for using AI Video Studio Professional!
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
