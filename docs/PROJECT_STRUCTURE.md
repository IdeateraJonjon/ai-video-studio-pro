# Project Structure Guide
## Understanding the AI Video Studio Architecture

### Directory Structure
```
C:\AI_Video_Generation\
├── studio_launch.py          # Main application launcher
├── setup_local_domain.ps1    # Local domain configuration
├── README.md                 # Complete documentation
├── video_studio.db          # SQLite database
├── templates/               # HTML templates
│   ├── dashboard.html       # Main dashboard
│   ├── projects.html        # Project management
│   ├── apis.html           # API configuration
│   └── github.html         # GitHub integration
├── outputs/                # Generated videos
├── models/                 # Local AI models
└── docs/                  # Additional documentation
    ├── API_INTEGRATION.md  # API setup guide
    ├── PROJECT_STRUCTURE.md # This file
    └── TROUBLESHOOTING.md  # Common issues
```

### Key Components

#### Application Core (`studio_launch.py`)
- **Flask Web Server** - Serves the web interface
- **Database Management** - SQLite operations
- **API Integration** - External service connections
- **File Management** - Video storage and organization

#### Templates (`templates/`)
- **Responsive Design** - Mobile-friendly interface
- **Cache Busting** - Always shows latest version
- **Real-time Updates** - Live progress tracking
- **Professional Styling** - Modern UI/UX

#### Database (`video_studio.db`)
- **Projects Table** - Organize video collections
- **Videos Table** - Track all generations
- **Relationships** - Video continuation chains
- **Metadata** - Settings and parameters

### Configuration Files

#### Hosts File Integration
The system can use custom local domains:
- `visual-video-studio.local:5000`
- `ai-video-studio.local:5000`
- `studio.local:5000`

#### PowerShell Setup Script
`setup_local_domain.ps1` configures:
- Custom domain entries
- DNS cache flushing
- Administrator permissions check
- Backup creation

### Data Flow

#### Video Generation Process
1. **User Input** → Web interface
2. **Queue Management** → Background processing
3. **API Selection** → HailuoAI/Veo2/Local
4. **Generation** → AI processing
5. **Storage** → Local files + database
6. **GitHub Upload** → Automatic sharing
7. **Notification** → User interface update

#### Project Management
1. **Project Creation** → Database entry
2. **Video Association** → Link to project
3. **Continuation Chain** → Parent-child relationships
4. **GitHub Repository** → Auto-creation
5. **Sharing** → Public URLs

### Customization Points

#### Adding New APIs
1. Create service class in `studio_launch.py`
2. Add configuration UI in `apis.html`
3. Update generation workflow
4. Test integration

#### Database Extensions
1. Modify table schemas
2. Update data access methods
3. Create migration scripts
4. Test backward compatibility

#### Interface Modifications
1. Update HTML templates
2. Modify CSS styling
3. Add JavaScript functionality
4. Test responsiveness