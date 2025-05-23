# FILE LOCATION GUIDE
## Where Everything Is Located

### 📁 Main Directory: `C:\AI_Video_Generation\`

## 🚀 KEY FILES TO USE:

### **Main Launchers:**
- **`launcher.bat`** ← **START HERE** (Menu system)
- **`studio_launch.py`** ← Standard server (port 5000)
- **`studio_production.py`** ← Production server (port 80)

### **Setup Files:**
- **`setup_domain.bat`** ← Run as Administrator for custom domains
- **`setup_local_domain.ps1`** ← PowerShell version (alternative)

### **Documentation:**
- **`README.md`** ← Complete guide (359 lines)
- **`QUICK_START.md`** ← 5-minute setup guide

## 📂 DIRECTORY STRUCTURE:

```
C:\AI_Video_Generation\
├── 🚀 launcher.bat              # MAIN MENU - START HERE
├── 🚀 studio_launch.py          # Server with :5000
├── 🚀 studio_production.py      # Server without :5000
├── 🔧 setup_domain.bat          # Domain setup (Run as Admin)
├── 📖 README.md                 # Complete documentation
├── ⚡ QUICK_START.md            # Quick setup guide
├── 🗄️ video_studio.db          # Your database
│
├── templates/                   # Web interface files
│   ├── dashboard.html           # Main dashboard
│   ├── projects.html            # Project management
│   ├── apis.html               # API configuration
│   └── github.html             # GitHub integration
│
├── docs/                       # Additional documentation
│   ├── GITHUB_GUIDE.md         # GitHub setup guide
│   ├── API_INTEGRATION.md      # API setup details
│   └── PROJECT_STRUCTURE.md    # Architecture guide
│
├── outputs/                    # Generated videos stored here
├── models/                     # AI models stored here
└── static/                     # Web assets
```

## 🎯 QUICK START COMMANDS:

### **Option 1: Use Menu System**
```cmd
cd C:\AI_Video_Generation
launcher.bat
```

### **Option 2: Direct Launch**
```cmd
cd C:\AI_Video_Generation
setup_domain.bat    (Run as Administrator first)
python studio_production.py    (Run as Administrator)
```

### **Option 3: Standard Launch**
```cmd
cd C:\AI_Video_Generation
python studio_launch.py
```

## 🔍 HOW TO FIND THESE FILES:

### **Method 1: File Explorer**
1. Open File Explorer
2. Navigate to: `C:\AI_Video_Generation\`
3. Look for the files listed above

### **Method 2: Command Line**
```cmd
cd C:\AI_Video_Generation
dir
```

### **Method 3: Search**
1. Press `Windows Key + S`
2. Search for "AI_Video_Generation"
3. Open the folder

## 📋 WHAT EACH FILE DOES:

### **Essential Files:**
- **`launcher.bat`** - Menu system to choose options
- **`setup_domain.bat`** - Sets up custom domains (visual-video-studio.local)
- **`studio_production.py`** - Runs server on port 80 (no :5000 needed)
- **`studio_launch.py`** - Runs server on port 5000

### **Generated Files:**
- **`video_studio.db`** - Your project and video database
- **`outputs/`** - Folder where generated videos are saved

### **Documentation:**
- **`README.md`** - Everything you need to know
- **`QUICK_START.md`** - Get started in 5 minutes
- **`docs/GITHUB_GUIDE.md`** - How GitHub integration works

## 🚨 IMPORTANT NOTES:

### **To Remove :5000 from URL:**
1. Run `setup_domain.bat` as Administrator
2. Run `python studio_production.py` as Administrator
3. Access: `http://visual-video-studio.local` (no port!)

### **For GitHub Integration:**
1. Go to: https://github.com/settings/tokens
2. Create Personal Access Token
3. Configure in studio at `/github-config` page

## 🎬 YOUR FILES ARE HERE:
**Main Folder:** `C:\AI_Video_Generation\`
**Start With:** `launcher.bat`
**Documentation:** `README.md`

---

**Everything is ready to use! 🚀**
