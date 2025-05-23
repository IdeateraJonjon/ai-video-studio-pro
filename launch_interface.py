"""
🌊 OCEAN VIDEO GENERATOR - LAUNCHER
==================================

This script launches the beautiful web interface for generating 
ocean pollution videos using AI.

Usage:
1. Run this script: python launch_interface.py
2. Open browser to: http://localhost:5000
3. Generate individual scenes or all at once
4. Download completed videos

Features:
✅ Beautiful web interface
✅ Real-time progress tracking  
✅ Individual scene generation
✅ Batch generation of all scenes
✅ Download completed videos
✅ Live status updates
"""

import os
import sys
import webbrowser
import time
import subprocess

def check_dependencies():
    """Check if all required packages are installed"""
    required = ['flask', 'torch', 'diffusers', 'transformers']
    missing = []
    
    for package in required:
        try:
            __import__(package)
        except ImportError:
            missing.append(package)
    
    if missing:
        print(f"❌ Missing packages: {', '.join(missing)}")
        print("🔧 Installing missing dependencies...")
        subprocess.run([sys.executable, '-m', 'pip', 'install'] + missing)
    else:
        print("✅ All dependencies installed!")

def launch_interface():
    """Launch the web interface"""
    print("🌊 OCEAN POLLUTION VIDEO GENERATOR")
    print("=" * 50)
    
    # Check dependencies
    check_dependencies()
    
    print("🖥️  Starting web interface...")
    print("📍 Opening browser to: http://localhost:5000")
    print("⏹️  Press Ctrl+C to stop the server")
    print()
    
    # Auto-open browser after a short delay
    def open_browser():
        time.sleep(2)
        webbrowser.open('http://localhost:5000')
    
    import threading
    browser_thread = threading.Thread(target=open_browser)
    browser_thread.daemon = True
    browser_thread.start()
    
    # Start the Flask app
    try:
        from web_interface import app
        app.run(debug=False, host='localhost', port=5000)
    except KeyboardInterrupt:
        print("\n👋 Interface stopped. Thanks for using Ocean Video Generator!")
    except Exception as e:
        print(f"❌ Error starting interface: {e}")
        print("💡 Try running: python web_interface.py")

if __name__ == "__main__":
    launch_interface()
