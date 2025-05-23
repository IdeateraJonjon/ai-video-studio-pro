# AI Video Studio Professional - Windows Installer
# Creates desktop shortcuts, start menu entries, and auto-startup

param(
    [string]$InstallPath = "C:\AI_Video_Studio_Pro",
    [switch]$CreateDesktopShortcut = $true,
    [switch]$CreateStartMenuEntry = $true,
    [switch]$AddToStartup = $false,
    [switch]$SetupDomains = $true
)

Write-Host "═══════════════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host "    AI VIDEO STUDIO PROFESSIONAL - INSTALLER v1.0" -ForegroundColor Yellow
Write-Host "═══════════════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host ""

# Check Administrator privileges
if (-NOT ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) {
    Write-Host "ERROR: This installer must be run as Administrator!" -ForegroundColor Red
    Write-Host "Right-click PowerShell and select 'Run as Administrator'" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "✓ Running as Administrator" -ForegroundColor Green

# Create installation directory
Write-Host "Creating installation directory..." -ForegroundColor Yellow
try {
    if (-not (Test-Path $InstallPath)) {
        New-Item -ItemType Directory -Path $InstallPath -Force | Out-Null
    }
    Write-Host "✓ Installation directory: $InstallPath" -ForegroundColor Green
} catch {
    Write-Host "✗ Failed to create installation directory: $_" -ForegroundColor Red
    exit 1
}

# Copy files to installation directory
Write-Host "Copying application files..." -ForegroundColor Yellow
try {
    $sourceDir = Split-Path -Parent $PSScriptRoot
    Copy-Item -Path "$sourceDir\*" -Destination $InstallPath -Recurse -Force -Exclude @("distribution", ".git")
    Write-Host "✓ Application files copied" -ForegroundColor Green
} catch {
    Write-Host "✗ Failed to copy files: $_" -ForegroundColor Red
    exit 1
}

# Setup custom domains
if ($SetupDomains) {
    Write-Host "Setting up custom domains..." -ForegroundColor Yellow
    try {
        $hostsFile = "$env:SystemRoot\System32\drivers\etc\hosts"
        $hostsContent = Get-Content $hostsFile -Raw
        
        if ($hostsContent -notmatch "visual-video-studio.local") {
            $domainEntries = @"

# AI Video Studio Professional - Local Development
127.0.0.1       visual-video-studio.local
127.0.0.1       ai-video-studio.local
127.0.0.1       studio.local
127.0.0.1       video-studio-pro.local
"@
            Add-Content $hostsFile $domainEntries
            # Flush DNS cache
            ipconfig /flushdns | Out-Null
            Write-Host "✓ Custom domains configured" -ForegroundColor Green
        } else {
            Write-Host "✓ Custom domains already configured" -ForegroundColor Green
        }
    } catch {
        Write-Host "✗ Failed to setup domains: $_" -ForegroundColor Red
    }
}

# Create desktop shortcut
if ($CreateDesktopShortcut) {
    Write-Host "Creating desktop shortcut..." -ForegroundColor Yellow
    try {
        $WScriptShell = New-Object -ComObject WScript.Shell
        $desktopPath = [Environment]::GetFolderPath("Desktop")
        $shortcut = $WScriptShell.CreateShortcut("$desktopPath\AI Video Studio Pro.lnk")
        $shortcut.TargetPath = "$InstallPath\launcher.bat"
        $shortcut.WorkingDirectory = $InstallPath
        $shortcut.Description = "AI Video Studio Professional - Create amazing AI videos"
        $shortcut.IconLocation = "$InstallPath\assets\icon.ico,0"
        $shortcut.Save()
        Write-Host "✓ Desktop shortcut created" -ForegroundColor Green
    } catch {
        Write-Host "✗ Failed to create desktop shortcut: $_" -ForegroundColor Red
    }
}

# Create Start Menu entry
if ($CreateStartMenuEntry) {
    Write-Host "Creating Start Menu entry..." -ForegroundColor Yellow
    try {
        $startMenuPath = [Environment]::GetFolderPath("CommonStartMenu") + "\Programs"
        $studioFolder = "$startMenuPath\AI Video Studio Pro"
        
        if (-not (Test-Path $studioFolder)) {
            New-Item -ItemType Directory -Path $studioFolder -Force | Out-Null
        }
        
        # Main application shortcut
        $WScriptShell = New-Object -ComObject WScript.Shell
        $shortcut = $WScriptShell.CreateShortcut("$studioFolder\AI Video Studio Pro.lnk")
        $shortcut.TargetPath = "$InstallPath\launcher.bat"
        $shortcut.WorkingDirectory = $InstallPath
        $shortcut.Description = "AI Video Studio Professional"
        $shortcut.Save()
        
        # Documentation shortcut
        $docShortcut = $WScriptShell.CreateShortcut("$studioFolder\Documentation.lnk")
        $docShortcut.TargetPath = "$InstallPath\README.md"
        $docShortcut.WorkingDirectory = $InstallPath
        $docShortcut.Description = "AI Video Studio Documentation"
        $docShortcut.Save()
        
        # Uninstaller shortcut
        $uninstallShortcut = $WScriptShell.CreateShortcut("$studioFolder\Uninstall.lnk")
        $uninstallShortcut.TargetPath = "$InstallPath\distribution\uninstall.ps1"
        $uninstallShortcut.WorkingDirectory = $InstallPath
        $uninstallShortcut.Description = "Uninstall AI Video Studio Pro"
        $uninstallShortcut.Save()
        
        Write-Host "✓ Start Menu entries created" -ForegroundColor Green
    } catch {
        Write-Host "✗ Failed to create Start Menu entry: $_" -ForegroundColor Red
    }
}

# Add to Windows startup (optional)
if ($AddToStartup) {
    Write-Host "Adding to Windows startup..." -ForegroundColor Yellow
    try {
        $startupPath = [Environment]::GetFolderPath("Startup")
        $WScriptShell = New-Object -ComObject WScript.Shell
        $shortcut = $WScriptShell.CreateShortcut("$startupPath\AI Video Studio Pro.lnk")
        $shortcut.TargetPath = "$InstallPath\auto_start.bat"
        $shortcut.WorkingDirectory = $InstallPath
        $shortcut.WindowStyle = 7  # Minimized
        $shortcut.Save()
        Write-Host "✓ Added to Windows startup" -ForegroundColor Green
    } catch {
        Write-Host "✗ Failed to add to startup: $_" -ForegroundColor Red
    }
}

# Create auto-start script
Write-Host "Creating auto-start configuration..." -ForegroundColor Yellow
try {
    $autoStartScript = @"
@echo off
title AI Video Studio Pro - Auto Start
cd /d "$InstallPath"
echo Starting AI Video Studio Professional...
echo Access at: http://visual-video-studio.local
python studio_production.py
"@
    $autoStartScript | Out-File -FilePath "$InstallPath\auto_start.bat" -Encoding ASCII
    Write-Host "✓ Auto-start script created" -ForegroundColor Green
} catch {
    Write-Host "✗ Failed to create auto-start script: $_" -ForegroundColor Red
}

# Create uninstaller
Write-Host "Creating uninstaller..." -ForegroundColor Yellow
try {
    $uninstallScript = @"
# AI Video Studio Professional - Uninstaller
Write-Host "Uninstalling AI Video Studio Professional..." -ForegroundColor Yellow

# Remove installation directory
if (Test-Path "$InstallPath") {
    Remove-Item -Path "$InstallPath" -Recurse -Force
    Write-Host "✓ Installation files removed" -ForegroundColor Green
}

# Remove desktop shortcut
`$desktopShortcut = [Environment]::GetFolderPath("Desktop") + "\AI Video Studio Pro.lnk"
if (Test-Path `$desktopShortcut) {
    Remove-Item `$desktopShortcut -Force
    Write-Host "✓ Desktop shortcut removed" -ForegroundColor Green
}

# Remove Start Menu entries
`$startMenuPath = [Environment]::GetFolderPath("CommonStartMenu") + "\Programs\AI Video Studio Pro"
if (Test-Path `$startMenuPath) {
    Remove-Item -Path `$startMenuPath -Recurse -Force
    Write-Host "✓ Start Menu entries removed" -ForegroundColor Green
}

# Remove startup entry
`$startupShortcut = [Environment]::GetFolderPath("Startup") + "\AI Video Studio Pro.lnk"
if (Test-Path `$startupShortcut) {
    Remove-Item `$startupShortcut -Force
    Write-Host "✓ Startup entry removed" -ForegroundColor Green
}

Write-Host "AI Video Studio Professional has been uninstalled." -ForegroundColor Green
Read-Host "Press Enter to exit"
"@
    $uninstallScript | Out-File -FilePath "$InstallPath\distribution\uninstall.ps1" -Encoding UTF8
    Write-Host "✓ Uninstaller created" -ForegroundColor Green
} catch {
    Write-Host "✗ Failed to create uninstaller: $_" -ForegroundColor Red
}

# Create Windows Registry entries
Write-Host "Creating Windows Registry entries..." -ForegroundColor Yellow
try {
    $regPath = "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\AIVideoStudioPro"
    New-Item -Path $regPath -Force | Out-Null
    Set-ItemProperty -Path $regPath -Name "DisplayName" -Value "AI Video Studio Professional"
    Set-ItemProperty -Path $regPath -Name "DisplayVersion" -Value "1.0.0"
    Set-ItemProperty -Path $regPath -Name "Publisher" -Value "AI Video Studio"
    Set-ItemProperty -Path $regPath -Name "InstallLocation" -Value $InstallPath
    Set-ItemProperty -Path $regPath -Name "UninstallString" -Value "powershell.exe -ExecutionPolicy Bypass -File `"$InstallPath\distribution\uninstall.ps1`""
    Set-ItemProperty -Path $regPath -Name "DisplayIcon" -Value "$InstallPath\assets\icon.ico"
    Write-Host "✓ Registry entries created" -ForegroundColor Green
} catch {
    Write-Host "✗ Failed to create registry entries: $_" -ForegroundColor Red
}

Write-Host ""
Write-Host "═══════════════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host "    INSTALLATION COMPLETE!" -ForegroundColor Green
Write-Host "═══════════════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host ""
Write-Host "✓ Installed to: $InstallPath" -ForegroundColor Green
Write-Host "✓ Desktop shortcut created" -ForegroundColor Green
Write-Host "✓ Start Menu entry created" -ForegroundColor Green
Write-Host "✓ Custom domains configured" -ForegroundColor Green
Write-Host "✓ Auto-start options available" -ForegroundColor Green
Write-Host ""
Write-Host "🚀 ACCESS YOUR STUDIO:" -ForegroundColor Yellow
Write-Host "   • Desktop: Double-click 'AI Video Studio Pro'" -ForegroundColor White
Write-Host "   • Start Menu: AI Video Studio Pro" -ForegroundColor White
Write-Host "   • Browser: http://visual-video-studio.local" -ForegroundColor White
Write-Host "   • Local: http://localhost" -ForegroundColor White
Write-Host ""
Write-Host "📖 DOCUMENTATION:" -ForegroundColor Yellow
Write-Host "   • Complete Guide: $InstallPath\README.md" -ForegroundColor White
Write-Host "   • Quick Start: $InstallPath\QUICK_START.md" -ForegroundColor White
Write-Host ""

Read-Host "Press Enter to launch AI Video Studio Pro"

# Launch the application
Start-Process -FilePath "$InstallPath\launcher.bat" -WorkingDirectory $InstallPath
