# AI Video Studio Professional

> **Professional AI video generation platform with database, APIs, and GitHub integration**

🎬 **Create stunning AI-powered videos** using multiple APIs (HailuoAI, Veo 2, Local models)  
🗄️ **Organize projects** with complete database tracking  
🐙 **Share instantly** with automatic GitHub integration  
🌐 **Professional interface** with custom domain support  

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com/)

## 🚀 Quick Start

### One-Click Installation (Windows)
1. **Download** the latest release
2. **Extract** to any folder
3. **Right-click** `INSTALL.bat` → "Run as administrator"
4. **Access** at `http://visual-video-studio.local`

### Manual Installation
```bash
git clone https://github.com/yourusername/ai-video-studio-pro.git
cd ai-video-studio-pro
pip install -r requirements.txt
python studio_launch.py
```

## ✨ Features

### 🤖 Multi-API Video Generation
- **HailuoAI** - Premium subscription service
- **Veo 2** - Google's advanced video AI
- **Local Models** - Stable Video Diffusion, AnimateDiff
- **Smart Switching** - Choose best API per project

### 📁 Project Management
- **Database-driven** organization
- **Video continuation** chains
- **Complete history** tracking
- **Metadata storage**

### 🐙 GitHub Integration
- **Auto-repository** creation
- **Public sharing** links  
- **Documentation** generation
- **Team collaboration**

### 🌐 Professional Interface
- **Custom domains** (visual-video-studio.local)
- **Real-time progress** tracking
- **Mobile responsive** design
- **Cache-busted** updates

## 📸 Screenshots

### Dashboard
![Dashboard](docs/images/dashboard.png)
*Main control center with project overview and quick actions*

### Project Management
![Projects](docs/images/projects.png)
*Organize and track your video generation projects*

### API Configuration
![APIs](docs/images/apis.png)
*Configure HailuoAI, Veo 2, and local models*

### GitHub Integration
![GitHub](docs/images/github.png)
*Automatic sharing and collaboration features*

## 🛠️ Installation Options

### Option 1: Windows Installer (Recommended)
```bash
# Download and run as Administrator
INSTALL.bat
```
**Features:**
- ✅ Desktop shortcut
- ✅ Start Menu entry  
- ✅ Custom domains setup
- ✅ Auto-start options
- ✅ Uninstaller included

### Option 2: Portable Version
```bash
# Extract and run
launcher.bat
```
**Features:**
- ✅ No installation required
- ✅ Run from any folder
- ✅ USB drive compatible

### Option 3: Developer Setup
```bash
git clone https://github.com/yourusername/ai-video-studio-pro.git
cd ai-video-studio-pro
pip install -r requirements.txt
python studio_launch.py
```

## 🔧 Configuration

### HailuoAI Setup
1. **Navigate** to `/apis` page
2. **Enter** your API key
3. **Test** connection
4. **Start** generating premium videos

### GitHub Integration
1. **Create** Personal Access Token
2. **Configure** in `/github-config`
3. **Videos** auto-upload to repositories
4. **Share** with public URLs

### Custom Domains
```bash
# Run as Administrator
setup_domain.bat
```
Access via:
- `http://visual-video-studio.local`
- `http://ai-video-studio.local`
- `http://studio.local`

## 📖 Documentation

- 📚 **[Complete Guide](README.md)** - Full documentation
- ⚡ **[Quick Start](QUICK_START.md)** - 5-minute setup
- 🔗 **[API Integration](docs/API_INTEGRATION.md)** - API setup details
- 🐙 **[GitHub Guide](docs/GITHUB_GUIDE.md)** - Sharing and collaboration
- 🏗️ **[Architecture](docs/PROJECT_STRUCTURE.md)** - Technical details

## 🎯 Use Cases

### Content Creation
- **YouTube videos** with AI generation
- **Social media** content at scale
- **Marketing campaigns** with variations
- **Educational** materials

### Professional Production
- **Client presentations** with HailuoAI quality
- **Product demos** and explainers  
- **Documentary** footage generation
- **Concept visualization**

### Collaboration
- **Team projects** with GitHub integration
- **Version control** for video iterations
- **Public portfolios** for showcasing work
- **Educational** sharing and tutorials

## 🏆 Advanced Features

### Video Continuation
```python
# Generate Scene 1
scene_1 = generate_video("Ocean paradise at sunrise")

# Continue seamlessly
scene_2 = continue_video(scene_1, "Plastic pollution appears")
```

### Project Organization
- **Categories** by theme or client
- **Tagging** system for organization
- **Search** and filter capabilities
- **Export** options for different formats

### Performance Optimization
- **GPU acceleration** for local models
- **Queue management** for batch processing
- **API load balancing** across providers
- **Caching** for faster iterations

## 🔒 Security & Privacy

### Local-First Architecture
- **Database** stored locally
- **API keys** never transmitted
- **Full control** over your data
- **No cloud dependencies**

### GitHub Security
- **Personal Access Tokens** only
- **Limited scope** permissions
- **User-controlled** repositories
- **Delete anytime**

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Development Setup
```bash
git clone https://github.com/yourusername/ai-video-studio-pro.git
cd ai-video-studio-pro
pip install -r requirements-dev.txt
python -m pytest tests/
```

### Reporting Issues
- 🐛 **Bug reports** via GitHub Issues
- 💡 **Feature requests** welcome
- 📖 **Documentation** improvements
- 🔒 **Security** issues via private contact

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Flask** - Web framework
- **SQLite** - Database engine
- **HailuoAI** - Premium video generation API
- **PyTorch** - Machine learning framework
- **GitHub** - Repository hosting and collaboration

## 📞 Support

- 📖 **Documentation** - Comprehensive guides included
- 💬 **Community** - GitHub Discussions
- 🐛 **Issues** - Bug reports and feature requests
- 📧 **Contact** - For enterprise support

---

**🎬 Start creating amazing AI videos today!**

[Download Latest Release](https://github.com/yourusername/ai-video-studio-pro/releases/latest) | [View Documentation](README.md) | [Report Issues](https://github.com/yourusername/ai-video-studio-pro/issues)
