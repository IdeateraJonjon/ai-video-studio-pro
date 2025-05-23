"""
Ocean Pollution Video Generator - Web Interface
Beautiful local web UI for generating AI videos
"""

from flask import Flask, render_template, request, jsonify, send_file
import os
import json
import threading
import time
from datetime import datetime

app = Flask(__name__)

# Global status for tracking generation
generation_status = {
    'running': False,
    'current_scene': 0,
    'total_scenes': 9,
    'progress': 0,
    'message': 'Ready to generate',
    'completed_videos': []
}

# Ocean pollution scenes
OCEAN_SCENES = [
    {
        'id': 1,
        'title': 'Pristine Paradise',
        'prompt': 'Pristine turquoise ocean at sunrise, aerial view, crystal clear water, cinematic',
        'description': 'Beautiful untouched ocean as it should be'
    },
    {
        'id': 2, 
        'title': 'Plastic Rain',
        'prompt': 'Plastic bottles falling like rain into ocean, environmental disaster, dramatic',
        'description': 'The moment paradise is destroyed'
    },
    {
        'id': 3,
        'title': 'Underwater Pollution', 
        'prompt': 'Underwater view of plastic debris cloud, pollution in clear water, shocking',
        'description': 'What lies beneath the surface'
    },
    {
        'id': 4,
        'title': 'Industrial Waste',
        'prompt': 'Garbage trucks dumping plastic waste, industrial documentary style, gritty',
        'description': '2,000 trucks worth daily'
    },
    {
        'id': 5,
        'title': 'Pacific Garbage Patch',
        'prompt': 'Aerial view Great Pacific Garbage Patch, massive plastic vortex, enormous scale',
        'description': '1.6 million sq km of floating trash'
    },
    {
        'id': 6,
        'title': 'Marine Life Struggle',
        'prompt': 'Sea turtle entangled in plastic nets, struggling underwater, heartbreaking',
        'description': '180x more plastic than marine life'
    },
    {
        'id': 7,
        'title': 'Human Impact Chain',
        'prompt': 'City to ocean pollution flow, fast montage consumption to waste, connection',
        'description': 'From our cities to their oceans'
    },
    {
        'id': 8,
        'title': 'Before vs After',
        'prompt': 'Split screen pristine vs polluted ocean, before and after comparison, dramatic',
        'description': '50 years of destruction'
    },
    {
        'id': 9,
        'title': 'Global Crisis',
        'prompt': 'Earth from space showing garbage patches, environmental overview, planetary',
        'description': 'A planet drowning in plastic'
    }
]

@app.route('/')
def index():
    return render_template('index.html', scenes=OCEAN_SCENES)

@app.route('/generate_scene', methods=['POST'])
def generate_scene():
    scene_id = request.json.get('scene_id')
    scene = next((s for s in OCEAN_SCENES if s['id'] == scene_id), None)
    
    if not scene:
        return jsonify({'error': 'Scene not found'})
    
    # Start generation in background thread
    thread = threading.Thread(target=generate_video_worker, args=(scene,))
    thread.start()
    
    return jsonify({'message': f'Started generating {scene["title"]}'})

@app.route('/generate_all', methods=['POST'])
def generate_all():
    # Start generation of all scenes
    thread = threading.Thread(target=generate_all_worker)
    thread.start()
    
    return jsonify({'message': 'Started generating all scenes'})

@app.route('/status')
def status():
    return jsonify(generation_status)

def generate_video_worker(scene):
    """Generate a single video scene"""
    global generation_status
    
    generation_status['running'] = True
    generation_status['message'] = f'Generating {scene["title"]}...'
    
    try:
        # Simulate video generation (replace with actual AI code)
        output_dir = 'generated_videos'
        os.makedirs(output_dir, exist_ok=True)
        
        # Here you would call the actual AI generation
        # For now, create a placeholder
        timestamp = datetime.now().strftime("%H%M%S")
        video_path = os.path.join(output_dir, f'scene_{scene["id"]:02d}_{timestamp}.mp4')
        
        # Simulate processing time
        for i in range(10):
            time.sleep(1)
            generation_status['progress'] = (i + 1) * 10
        
        # Mark as completed
        generation_status['completed_videos'].append({
            'scene': scene['title'],
            'path': video_path,
            'timestamp': timestamp
        })
        
        generation_status['message'] = f'Completed {scene["title"]}'
        
    except Exception as e:
        generation_status['message'] = f'Error: {str(e)}'
    
    generation_status['running'] = False
    generation_status['progress'] = 0

def generate_all_worker():
    """Generate all video scenes"""
    global generation_status
    
    generation_status['running'] = True
    generation_status['total_scenes'] = len(OCEAN_SCENES)
    generation_status['current_scene'] = 0
    
    for scene in OCEAN_SCENES:
        generation_status['current_scene'] = scene['id']
        generation_status['message'] = f'Generating Scene {scene["id"]}: {scene["title"]}'
        
        # Generate scene (simplified for demo)
        time.sleep(5)  # Simulate generation time
        
        generation_status['completed_videos'].append({
            'scene': scene['title'],
            'path': f'scene_{scene["id"]:02d}.mp4',
            'timestamp': datetime.now().strftime("%H%M%S")
        })
    
    generation_status['running'] = False
    generation_status['message'] = 'All scenes completed!'

if __name__ == '__main__':
    # Create templates directory and HTML
    os.makedirs('templates', exist_ok=True)
    
    print("Ocean Pollution Video Generator")
    print("=" * 50)
    print("Starting web interface...")
    print("Open your browser to: http://localhost:5000")
    print("Press Ctrl+C to stop")
    
    app.run(debug=True, host='localhost', port=5000)
