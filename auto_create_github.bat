@echo off
title AI Video Studio - Automated GitHub Repository Creator
color 0B
echo.
echo ╔══════════════════════════════════════════════════════════════╗
echo ║         🤖 FULLY AUTOMATED GITHUB REPOSITORY CREATOR        ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.
echo This will create your GitHub repository COMPLETELY AUTOMATICALLY!
echo.
echo 📋 What you need:
echo • GitHub username
echo • Personal Access Token (I'll help you get this)
echo.
echo 🚀 What this script does:
echo ✓ Creates GitHub repository automatically
echo ✓ Sets up all connections
echo ✓ Pushes all 43 files to GitHub
echo ✓ Makes your project publicly available
echo ✓ Opens repository when done
echo.
echo 💡 FIRST TIME SETUP: Get Personal Access Token
echo.
set /p first_time="Is this your first time? Need help getting token? (y/n): "

if /i "%first_time%"=="y" (
    echo.
    echo 🌐 Opening GitHub token creation page...
    start "GitHub Token" "https://github.com/settings/tokens/new?scopes=repo&description=AI+Video+Studio"
    echo.
    echo 📋 INSTRUCTIONS IN THE BROWSER:
    echo 1. ✓ Token name: "AI Video Studio" (pre-filled)
    echo 2. ✓ Expiration: No expiration (or your choice)
    echo 3. ✓ Scopes: "repo" should be checked (pre-filled)
    echo 4. 👆 Click "Generate token"
    echo 5. 📋 COPY THE TOKEN (you won't see it again!)
    echo.
    echo ⏳ After you get your token, come back here...
    pause
)

echo.
echo 🚀 Starting Python automation script...
echo.
python create_github_repo.py

if %errorLevel% == 0 (
    echo.
    echo ╔══════════════════════════════════════════════════════════════╗
    echo ║                    🎉 REPOSITORY CREATED!                   ║
    echo ╚══════════════════════════════════════════════════════════════╝
    echo.
    echo Your AI Video Studio is now:
    echo ✓ Live on GitHub as a professional repository
    echo ✓ 43+ files published with complete documentation
    echo ✓ Ready for sharing and collaboration
    echo ✓ Perfect for your portfolio
    echo.
) else (
    echo.
    echo ⚠ Something went wrong. Common issues:
    echo • Invalid token or username
    echo • Network connection issues
    echo • Repository already exists
    echo.
    echo 💡 You can also use GitHub Desktop manually if needed.
)

echo.
echo 🎬 Would you like to launch AI Video Studio now?
set /p launch="Launch studio? (y/n): "

if /i "%launch%"=="y" (
    echo.
    echo Starting AI Video Studio Professional...
    start "" launcher.bat
)

echo.
echo Thank you for using AI Video Studio Professional! 🚀
pause
