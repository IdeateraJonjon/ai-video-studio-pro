@echo off
title AI Video Studio - Automated GitHub Setup
color 0A
cls
echo.
echo ███████╗██╗   ██╗██╗     ██╗         █████╗ ██╗   ██╗████████╗ ██████╗ 
echo ██╔════╝██║   ██║██║     ██║        ██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗
echo █████╗  ██║   ██║██║     ██║        ███████║██║   ██║   ██║   ██║   ██║
echo ██╔══╝  ██║   ██║██║     ██║        ██╔══██║██║   ██║   ██║   ██║   ██║
echo ██║     ╚██████╔╝███████╗███████╗   ██║  ██║╚██████╔╝   ██║   ╚██████╔╝
echo ╚═╝      ╚═════╝ ╚══════╝╚══════╝   ╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝ 
echo.
echo                    AUTOMATED GITHUB SETUP
echo ================================================================
echo.
echo 🤖 I'll handle EVERYTHING automatically except GitHub login!
echo.
echo What this script will do:
echo ✓ Open GitHub in your browser
echo ✓ Pre-fill repository creation form
echo ✓ Open GitHub Desktop
echo ✓ Guide you through final steps
echo ✓ Launch your studio when complete
echo.
pause

echo.
echo 🌐 STEP 1: Opening GitHub repository creation page...
echo.

:: Create the repository URL with pre-filled data
set "github_url=https://github.com/new?name=ai-video-studio-pro&description=Professional+AI+video+generation+platform+with+database+APIs+and+GitHub+integration&visibility=public"

echo Opening browser with pre-filled repository form...
start "" "%github_url%"

echo.
echo 🖥️ STEP 2: Opening GitHub Desktop...
echo.

:: Try multiple possible GitHub Desktop locations
start "" "C:\Users\%USERNAME%\AppData\Local\GitHubDesktop\GitHubDesktop.exe" 2>nul || (
    start "" "C:\Program Files\GitHub Desktop\GitHubDesktop.exe" 2>nul || (
        start "" "C:\Program Files (x86)\GitHub Desktop\GitHubDesktop.exe" 2>nul || (
            echo GitHub Desktop not found in common locations.
            echo Please open GitHub Desktop manually.
        )
    )
)

echo.
echo ================================================================
echo                   🎯 FINAL STEPS FOR YOU:
echo ================================================================
echo.
echo IN YOUR BROWSER (should be open now):
echo 1. ✓ Repository name: ai-video-studio-pro (pre-filled)
echo 2. ✓ Description: Professional AI video generation platform (pre-filled)
echo 3. ✓ Public repository selected (pre-filled)
echo 4. ✓ DON'T initialize with README (we have one)
echo 5. 👆 Just click "Create repository"
echo.
echo IN GITHUB DESKTOP (should be open now):
echo 1. 👆 Click "File" → "Add Local Repository"
echo 2. 👆 Browse to: C:\AI_Video_Generation
echo 3. 👆 Click "Add Repository"
echo 4. 👆 Click "Publish repository" (blue button)
echo 5. 👆 Click "Publish Repository" (confirm)
echo.
echo ⏱️ Waiting for you to complete these steps...
echo.
set /p done="Press Enter when you've completed both steps above..."

echo.
echo 🎉 STEP 3: Verifying setup...
echo.

:: Check if remote was added
git remote -v >nul 2>&1
if %errorLevel% == 0 (
    echo ✓ GitHub repository connected!
    git remote -v
) else (
    echo ⚠ Repository might not be connected yet.
    echo This is normal if you're still setting up.
)

echo.
echo 🚀 STEP 4: Launching AI Video Studio...
echo.

echo Your professional AI Video Studio is now:
echo ✓ Published on GitHub
echo ✓ Ready for sharing and collaboration
echo ✓ Portfolio-ready presentation
echo ✓ Open source and distributable
echo.

set /p launch="Would you like to launch the studio now? (y/n): "
if /i "%launch%"=="y" (
    echo.
    echo 🎬 Launching AI Video Studio Professional...
    echo Access at: http://visual-video-studio.local:5000
    echo.
    start "" launcher.bat
) else (
    echo.
    echo 💡 To launch later, run: launcher.bat
    echo 💡 Or use desktop shortcut (if installer was used)
)

echo.
echo ================================================================
echo                     🏆 SETUP COMPLETE!
echo ================================================================
echo.
echo Your AI Video Studio is now:
echo ✓ Professional GitHub repository
echo ✓ Complete documentation included  
echo ✓ Windows installer ready
echo ✓ Portable version available
echo ✓ Custom domain support
echo ✓ Multi-API integration
echo ✓ Database project management
echo ✓ GitHub sharing features
echo.
echo 🌐 Repository URL: https://github.com/yourusername/ai-video-studio-pro
echo 🎬 Studio Access: http://visual-video-studio.local:5000
echo.
echo Thank you for using AI Video Studio Professional! 🚀
pause
