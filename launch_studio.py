"""
Enhanced AI Video Studio Launcher
Professional interface with advanced features
"""

import os
import sys
import webbrowser
import time
import subprocess

def install_dependencies():
    """Install required packages"""
    required = ['flask', 'psutil', 'torch', 'diffusers', 'transformers']
    print("Checking dependencies...")
    
    for package in required:
        try:
            __import__(package)
            print(f"✓ {package}")
        except ImportError:
            print(f"Installing {package}...")
            subprocess.run([sys.executable, '-m', 'pip', 'install', package])

def launch_enhanced_studio():
    """Launch the enhanced AI video studio"""
    print("AI VIDEO STUDIO - ENHANCED VERSION")
    print("=" * 50)
    print("Features:")
    print("- Professional web interface")
    print("- Model management system")
    print("- System monitoring")
    print("- Custom video creation")
    print("- Real-time progress tracking")
    print()
    
    install_dependencies()
    
    print("Starting enhanced web interface...")
    print("Open: http://localhost:5000")
    print("Press Ctrl+C to stop")
    print()
    
    # Auto-open browser
    def open_browser():
        time.sleep(3)
        webbrowser.open('http://localhost:5000')
    
    import threading
    browser_thread = threading.Thread(target=open_browser)
    browser_thread.daemon = True
    browser_thread.start()
    
    # Start enhanced interface
    try:
        os.system('python enhanced_web_interface.py')
    except KeyboardInterrupt:
        print("Studio stopped!")

if __name__ == "__main__":
    launch_enhanced_studio()
