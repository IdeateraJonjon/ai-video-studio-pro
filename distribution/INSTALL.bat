@echo off
title AI Video Studio Professional - One-Click Installer
color 0B
echo.
echo  ╔══════════════════════════════════════════════════════════════╗
echo  ║           AI VIDEO STUDIO PROFESSIONAL INSTALLER            ║
echo  ║                        Version 1.0                          ║
echo  ╚══════════════════════════════════════════════════════════════╝
echo.
echo  This installer will:
echo  • Install AI Video Studio to C:\AI_Video_Studio_Pro
echo  • Create desktop shortcut
echo  • Add Start Menu entries
echo  • Setup custom domains (visual-video-studio.local)
echo  • Configure auto-start options
echo.
echo  IMPORTANT: Must be run as Administrator!
echo.
pause

echo Checking administrator privileges...
net session >nul 2>&1
if %errorLevel% == 0 (
    echo ✓ Running as Administrator
) else (
    echo ✗ ERROR: Must run as Administrator!
    echo.
    echo Right-click this file and select "Run as administrator"
    pause
    exit /b 1
)

echo.
echo Starting PowerShell installer...
echo.

powershell.exe -ExecutionPolicy Bypass -File "%~dp0install.ps1"

if %errorLevel% == 0 (
    echo.
    echo ╔══════════════════════════════════════════════════════════════╗
    echo ║                   INSTALLATION SUCCESSFUL!                  ║
    echo ╚══════════════════════════════════════════════════════════════╝
    echo.
    echo ✓ AI Video Studio Professional is now installed
    echo ✓ Check your desktop for the shortcut
    echo ✓ Access via: http://visual-video-studio.local
    echo.
) else (
    echo.
    echo ✗ Installation failed. Check error messages above.
    echo.
)

pause
