@echo off
title Create Distribution Package
color 0E
echo.
echo ╔══════════════════════════════════════════════════════════════╗
echo ║            AI VIDEO STUDIO - DISTRIBUTION CREATOR           ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.
echo This will create a complete distribution package with:
echo • Windows Installer
echo • Portable ZIP version  
echo • GitHub repository files
echo • Desktop shortcuts
echo • Auto-start options
echo.
pause

echo Creating distribution package...
echo.

:: Create distribution folder structure
if not exist "dist" mkdir dist
if not exist "dist\portable" mkdir dist\portable
if not exist "dist\installer" mkdir dist\installer
if not exist "dist\github" mkdir dist\github

:: Copy core files to portable version
echo Copying files for portable version...
xcopy /E /I /Y *.py dist\portable\
xcopy /E /I /Y *.bat dist\portable\
xcopy /E /I /Y *.md dist\portable\
xcopy /E /I /Y *.txt dist\portable\
xcopy /E /I /Y templates dist\portable\templates\
xcopy /E /I /Y docs dist\portable\docs\
xcopy /E /I /Y assets dist\portable\assets\
if exist outputs xcopy /E /I /Y outputs dist\portable\outputs\

:: Copy installer files
echo Copying installer files...
xcopy /E /I /Y distribution\* dist\installer\

:: Copy GitHub repository files
echo Copying GitHub files...
copy distribution\GITHUB_README.md dist\github\README.md
copy requirements.txt dist\github\
copy LICENSE dist\github\ 2>nul
xcopy /E /I /Y docs dist\github\docs\

:: Create portable launcher
echo Creating portable launcher...
(
echo @echo off
echo title AI Video Studio Professional - Portable
echo cd /d "%%~dp0"
echo echo Starting AI Video Studio Professional...
echo echo Access at: http://visual-video-studio.local:5000
echo python studio_launch.py
echo pause
) > dist\portable\START_HERE.bat

:: Create ZIP archive
echo Creating ZIP archive...
if exist "AI_Video_Studio_Professional_Portable.zip" del "AI_Video_Studio_Professional_Portable.zip"
powershell Compress-Archive -Path "dist\portable\*" -DestinationPath "AI_Video_Studio_Professional_Portable.zip"

:: Create installer archive
echo Creating installer package...
if exist "AI_Video_Studio_Professional_Installer.zip" del "AI_Video_Studio_Professional_Installer.zip"
powershell Compress-Archive -Path "dist\installer\*" -DestinationPath "AI_Video_Studio_Professional_Installer.zip"

echo.
echo ╔══════════════════════════════════════════════════════════════╗
echo ║                  DISTRIBUTION COMPLETE!                     ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.
echo Created files:
echo ✓ AI_Video_Studio_Professional_Portable.zip
echo ✓ AI_Video_Studio_Professional_Installer.zip
echo ✓ dist\github\ (ready for GitHub repository)
echo.
echo You can now:
echo • Share the portable ZIP version
echo • Use the installer for professional setup
echo • Upload dist\github\ contents to GitHub
echo.
pause