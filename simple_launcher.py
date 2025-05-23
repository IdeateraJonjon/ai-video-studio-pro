"""
OCEAN VIDEO GENERATOR - Web Interface Launcher
==============================================
"""

import os
import sys
import webbrowser
import time
import subprocess

def launch_interface():
    print("OCEAN POLLUTION VIDEO GENERATOR")
    print("=" * 50)
    print("Starting web interface...")
    print("Open browser to: http://localhost:5000")
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
    
    # Start Flask app
    try:
        os.system('python web_interface.py')
    except KeyboardInterrupt:
        print("Interface stopped!")

if __name__ == "__main__":
    launch_interface()
