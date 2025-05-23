@echo off
title GitHub Repository Setup
color 0B
echo.
echo ╔══════════════════════════════════════════════════════════════╗
echo ║              GITHUB REPOSITORY SETUP GUIDE                  ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.
echo ✓ Local Git repository initialized
echo ✓ Initial commit created (43 files, 7305+ lines)
echo ✓ Professional README.md created
echo ✓ MIT License added
echo ✓ Contributing guidelines included
echo ✓ .gitignore configured
echo.
echo 🚀 NEXT STEPS TO CREATE GITHUB REPOSITORY:
echo.
echo 1. GO TO GITHUB.COM
echo    • Sign in to your GitHub account
echo    • Click the "+" icon → "New repository"
echo.
echo 2. REPOSITORY SETTINGS:
echo    • Repository name: ai-video-studio-pro
echo    • Description: Professional AI video generation platform
echo    • Public repository (recommended for sharing)
echo    • DO NOT initialize with README (we already have one)
echo.
echo 3. COPY THE REPOSITORY URL:
echo    • Example: https://github.com/USERNAME/ai-video-studio-pro.git
echo.
echo 4. RUN THESE COMMANDS:
echo    • git remote add origin YOUR_REPO_URL
echo    • git branch -M main
echo    • git push -u origin main
echo.
echo 🎯 QUICK SETUP COMMANDS (replace YOUR_REPO_URL):
echo.
echo git remote add origin https://github.com/USERNAME/ai-video-studio-pro.git
echo git branch -M main
echo git push -u origin main
echo.
echo ═══════════════════════════════════════════════════════════════
echo.
set /p repo_url="Enter your GitHub repository URL (or press Enter to skip): "

if "%repo_url%"=="" (
    echo.
    echo Skipping automatic setup. Use the commands above manually.
    goto end
)

echo.
echo Adding remote origin...
git remote add origin %repo_url%

echo Renaming branch to main...
git branch -M main

echo Pushing to GitHub...
git push -u origin main

if %errorLevel% == 0 (
    echo.
    echo ╔══════════════════════════════════════════════════════════════╗
    echo ║                REPOSITORY CREATED SUCCESSFULLY!             ║
    echo ╚══════════════════════════════════════════════════════════════╝
    echo.
    echo ✓ Repository pushed to GitHub
    echo ✓ Professional presentation ready
    echo ✓ Documentation included
    echo ✓ Ready for sharing and collaboration
    echo.
    echo 🌐 Your repository is now live at:
    echo %repo_url%
    echo.
) else (
    echo.
    echo ✗ Push failed. Common issues:
    echo   • Repository URL incorrect
    echo   • Repository already initialized with files
    echo   • Authentication required
    echo.
    echo Try creating an empty repository on GitHub and try again.
)

:end
echo.
echo 📖 WHAT'S INCLUDED IN YOUR REPOSITORY:
echo.
echo ✓ Complete AI Video Studio source code
echo ✓ Professional README with features and screenshots
echo ✓ Installation instructions (Windows installer)
echo ✓ API integration guides (HailuoAI, Veo 2)
echo ✓ GitHub integration documentation
echo ✓ Contributing guidelines
echo ✓ MIT License for open source sharing
echo ✓ Requirements.txt for easy installation
echo ✓ Professional project structure
echo.
echo 🚀 REPOSITORY FEATURES:
echo   • One-click Windows installer
echo   • Portable version support
echo   • Custom domain setup
echo   • Multi-API video generation
echo   • Database project management
echo   • GitHub integration for sharing
echo   • Professional documentation
echo.
pause