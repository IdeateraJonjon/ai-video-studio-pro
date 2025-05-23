@echo off
echo AI Video Studio - Domain Setup
echo ================================
echo.

:: Check if running as Administrator
net session >nul 2>&1
if %errorLevel% == 0 (
    echo Running as Administrator... Good!
) else (
    echo ERROR: This script must be run as Administrator!
    echo Right-click this file and select "Run as administrator"
    pause
    exit /b 1
)

:: Backup hosts file
copy "%SystemRoot%\System32\drivers\etc\hosts" "%TEMP%\hosts_backup_%date:~-4,4%%date:~-10,2%%date:~-7,2%.txt"
echo Hosts file backed up to %TEMP%

:: Check if entries already exist
findstr /C:"visual-video-studio.local" "%SystemRoot%\System32\drivers\etc\hosts" >nul
if %errorLevel% == 0 (
    echo Custom domains already configured!
) else (
    echo Adding custom domains to hosts file...
    echo. >> "%SystemRoot%\System32\drivers\etc\hosts"
    echo # AI Video Studio Professional - Local Development >> "%SystemRoot%\System32\drivers\etc\hosts"
    echo 127.0.0.1       visual-video-studio.local >> "%SystemRoot%\System32\drivers\etc\hosts"
    echo 127.0.0.1       ai-video-studio.local >> "%SystemRoot%\System32\drivers\etc\hosts"
    echo 127.0.0.1       studio.local >> "%SystemRoot%\System32\drivers\etc\hosts"
    echo Custom domains added successfully!
)

:: Flush DNS cache
echo Flushing DNS cache...
ipconfig /flushdns >nul

echo.
echo Setup complete! You can now use:
echo   http://visual-video-studio.local:5000
echo   http://ai-video-studio.local:5000
echo   http://studio.local:5000
echo.
echo Starting AI Video Studio...
pause
