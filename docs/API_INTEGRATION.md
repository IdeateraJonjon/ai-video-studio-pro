# API Integration Guide
## Connecting External Video Generation Services

### HailuoAI Integration

HailuoAI offers premium video generation with high quality output. Since you have a subscription, this is your primary production API.

#### Setup Process
1. **Obtain API Key**
   - Log into your HailuoAI dashboard
   - Navigate to API section
   - Generate or copy your API key

2. **Configure in Studio**
   - Go to `http://visual-video-studio.local:5000/apis`
   - Paste your API key in HailuoAI section
   - Click "Configure HailuoAI"
   - Status should change to "Active"

3. **Usage**
   - Select "HailuoAI" when generating videos
   - Higher quality but longer processing time
   - Costs based on your subscription plan

### Video Continuation Feature

One of the most powerful features is the ability to continue videos from previous scenes.

#### How It Works
1. **Generate Initial Video** - Create your first scene
2. **Select Continue Option** - Choose "Continue from this video"
3. **Automatic Context** - System remembers previous scene
4. **Seamless Flow** - New video continues story/action
5. **Chain Tracking** - Database maintains video relationships

#### Use Cases
- **Storytelling** - Multi-part narratives
- **Tutorials** - Sequential lessons
- **Marketing** - Campaign series
- **Documentation** - Step-by-step guides

### GitHub Integration Benefits

#### Automatic Sharing
- **Repository Creation** - One repo per project
- **File Organization** - Structured folders
- **Public Access** - Instant sharing links
- **Version Control** - Track changes over time

#### Professional Presentation
- **Auto-generated READMEs** - Project documentation
- **Thumbnail Previews** - Video previews in GitHub
- **Collaborative Access** - Team sharing
- **Portfolio Building** - Showcase your work