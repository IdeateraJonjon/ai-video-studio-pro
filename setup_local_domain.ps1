# AI Video Studio - Local Domain Setup
# Run this script as Administrator to add custom local domain

Write-Host "AI Video Studio - Local Domain Configuration" -ForegroundColor Cyan
Write-Host "=" * 50

# Check if running as Administrator
if (-NOT ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) {
    Write-Host "ERROR: This script must be run as Administrator!" -ForegroundColor Red
    Write-Host "Right-click PowerShell and select 'Run as Administrator'" -ForegroundColor Yellow
    pause
    exit
}

$hostsFile = "$env:SystemRoot\System32\drivers\etc\hosts"
$newEntries = @"

# AI Video Studio Professional - Local Development
127.0.0.1       visual-video-studio.local
127.0.0.1       ai-video-studio.local  
127.0.0.1       video-studio-pro.local
127.0.0.1       studio.local

"@

try {
    # Backup original hosts file
    $backup = "$env:TEMP\hosts_backup_$(Get-Date -Format 'yyyyMMdd_HHmmss').txt"
    Copy-Item $hostsFile $backup
    Write-Host "Backup created: $backup" -ForegroundColor Green

    # Check if entries already exist
    $currentContent = Get-Content $hostsFile -Raw
    if ($currentContent -notmatch "visual-video-studio.local") {
        # Add new entries
        Add-Content $hostsFile $newEntries
        Write-Host "Successfully added custom domains to hosts file!" -ForegroundColor Green
        Write-Host ""
        Write-Host "Available domains:" -ForegroundColor Yellow
        Write-Host "  http://visual-video-studio.local:5000" -ForegroundColor Cyan
        Write-Host "  http://ai-video-studio.local:5000" -ForegroundColor Cyan
        Write-Host "  http://video-studio-pro.local:5000" -ForegroundColor Cyan
        Write-Host "  http://studio.local:5000" -ForegroundColor Cyan
        Write-Host ""
        Write-Host "You can now use these domains in your browser!" -ForegroundColor Green
    } else {
        Write-Host "Custom domains already exist in hosts file." -ForegroundColor Yellow
    }

    # Flush DNS cache
    Write-Host "Flushing DNS cache..." -ForegroundColor Yellow
    ipconfig /flushdns | Out-Null
    Write-Host "DNS cache flushed successfully!" -ForegroundColor Green

} catch {
    Write-Host "Error: $($_.Exception.Message)" -ForegroundColor Red
}

Write-Host ""
Write-Host "Setup complete! Start your AI Video Studio and visit:" -ForegroundColor Green
Write-Host "http://visual-video-studio.local:5000" -ForegroundColor Cyan
Write-Host ""
pause