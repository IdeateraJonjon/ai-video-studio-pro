# GitHub Integration Guide
## How Video Sharing Works

### What GitHub Integration Does

#### Automatic Repository Creation
When you enable GitHub integration, the system:

1. **Creates repositories** automatically for each project
2. **Names them** like: `ai-videos-ocean-pollution`
3. **Makes them public** for easy sharing
4. **Organizes videos** in structured folders

#### Video Upload Process
```
Your Generated Video
       ↓
Local Storage (outputs/)
       ↓
GitHub API Upload
       ↓
Public Repository
       ↓
Shareable URL
```

#### Repository Structure
```
ai-videos-ocean-pollution/
├── README.md                    # Auto-generated description
├── videos/
│   ├── scene_01_pristine_ocean.mp4
│   ├── scene_02_plastic_rain.mp4
│   └── scene_03_underwater_pollution.mp4
├── prompts/
│   ├── scene_01_prompt.txt
│   └── scene_02_prompt.txt
└── project_info.json           # Project metadata
```

### Setup Process

#### 1. Create Personal Access Token
1. **Go to**: https://github.com/settings/tokens
2. **Click**: "Generate new token (classic)"
3. **Set expiration**: No expiration (for convenience)
4. **Select scopes**:
   - ✅ `repo` (Full control of private repositories)
   - ✅ `user` (Update user information)
5. **Generate token**
6. **Copy token** immediately (you won't see it again!)

#### 2. Configure in Studio
1. **Navigate** to GitHub page in studio
2. **Enter** your GitHub username
3. **Paste** the personal access token
4. **Click** "Connect GitHub Integration"
5. **Verify** status shows "Connected"

### Benefits of GitHub Integration

#### Professional Sharing
- **Public URLs** for instant sharing
- **Portfolio building** with organized repositories
- **Collaboration** with team members
- **Version control** for video iterations

#### Automatic Documentation
- **README files** with project descriptions
- **Video catalogs** with thumbnails
- **Prompt documentation** for reproducibility
- **Project metadata** for organization

#### Example Shared URLs
After upload, you get URLs like:
- `https://github.com/yourusername/ai-videos-ocean-pollution`
- `https://github.com/yourusername/ai-videos-marketing-campaign`

### Privacy Considerations

#### What Gets Uploaded
- ✅ Video files (MP4)
- ✅ Project descriptions
- ✅ Video prompts (for transparency)
- ✅ Generation metadata

#### What Stays Private
- ❌ API keys (never uploaded)
- ❌ Personal settings
- ❌ Local configuration
- ❌ Database contents

#### Repository Visibility
- **Default**: Public (for sharing)
- **Option**: Private repositories (paid GitHub plans)
- **Control**: You own all repositories
- **Management**: Delete/modify anytime

### Troubleshooting GitHub

#### Common Issues

**Token Permission Error**
- Verify token has `repo` and `user` scopes
- Check token hasn't expired
- Ensure username matches token owner

**Upload Failures**
- Check internet connection
- Verify file size limits (100MB per file)
- Ensure repository name is valid

**Repository Not Found**
- System creates repositories automatically
- Check GitHub account for new repositories
- Verify username is correct

#### Success Indicators
- ✅ Status shows "GitHub Connected"
- ✅ Videos appear in your GitHub repositories
- ✅ Public URLs work when shared
- ✅ README files are auto-generated

### Advanced GitHub Features

#### Collaboration
- **Add collaborators** to repositories
- **Team access** for organizations
- **Issue tracking** for feedback
- **Pull requests** for improvements

#### Portfolio Building
- **Pin repositories** to profile
- **Add descriptions** and topics
- **Showcase work** to potential clients
- **Build reputation** in AI video creation

#### Integration with Other Tools
- **Embed videos** in websites
- **Link to social media** 
- **Reference in presentations**
- **Share in portfolios**

---

## Quick GitHub Setup Checklist

- [ ] Go to https://github.com/settings/tokens
- [ ] Create new token with `repo` and `user` scopes
- [ ] Copy token immediately
- [ ] Navigate to GitHub page in studio
- [ ] Enter username and token
- [ ] Test connection
- [ ] Generate first video
- [ ] Verify auto-upload to GitHub
- [ ] Share public repository URL

**Your videos will be automatically shared to GitHub! 🚀**