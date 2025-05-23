"""
Enhanced Ocean Video Generator - Professional Interface
Advanced features: Model management, system status, custom videos
"""

from flask import Flask, render_template, request, jsonify, send_file
import os
import json
import threading
import time
import psutil
import torch
import platform
from datetime import datetime
import subprocess
import sys

app = Flask(__name__)

# Global status and configuration
app_status = {
    'generation': {
        'running': False,
        'current_scene': 0,
        'total_scenes': 9,
        'progress': 0,
        'message': 'Ready to generate',
        'completed_videos': [],
        'queue': []
    },
    'system': {
        'cpu_percent': 0,
        'memory_percent': 0,
        'disk_usage': 0,
        'gpu_available': torch.cuda.is_available(),
        'torch_version': torch.__version__,
        'python_version': platform.python_version(),
        'os_info': platform.platform()
    },
    'models': {
        'available': [
            {
                'name': 'Stable Video Diffusion',
                'id': 'svd',
                'size': '7.2 GB',
                'quality': 'High',
                'speed': 'Slow',
                'description': 'Best quality video generation, slower processing',
                'installed': False,
                'downloading': False
            },
            {
                'name': 'AnimateDiff',
                'id': 'animatediff', 
                'size': '3.8 GB',
                'quality': 'Medium-High',
                'speed': 'Medium',
                'description': 'Good balance of quality and speed',
                'installed': False,
                'downloading': False
            },
            {
                'name': 'Text2Video-Zero',
                'id': 't2v-zero',
                'size': '2.1 GB', 
                'quality': 'Medium',
                'speed': 'Fast',
                'description': 'Fastest generation, good for testing',
                'installed': False,
                'downloading': False
            },
            {
                'name': 'ModelScope T2V',
                'id': 'modelscope',
                'size': '4.5 GB',
                'quality': 'High',
                'speed': 'Medium',
                'description': 'Excellent for realistic scenes',
                'installed': False,
                'downloading': False
            }
        ],
        'active_model': None
    },
    'settings': {
        'output_resolution': '512x512',
        'fps': 8,
        'duration': 6,
        'inference_steps': 25,
        'guidance_scale': 7.5,
        'output_format': 'mp4'
    }
}

# Enhanced scene database
SCENE_CATEGORIES = {
    'ocean_pollution': {
        'name': 'Ocean Pollution Crisis',
        'scenes': [
            {
                'id': 1,
                'title': 'Pristine Paradise',
                'prompt': 'Pristine turquoise ocean at sunrise, aerial view, crystal clear water, cinematic',
                'description': 'Beautiful untouched ocean as it should be',
                'tags': ['ocean', 'pristine', 'nature']
            },
            {
                'id': 2,
                'title': 'Plastic Rain', 
                'prompt': 'Plastic bottles falling like rain into ocean, environmental disaster, dramatic',
                'description': 'The moment paradise is destroyed',
                'tags': ['pollution', 'plastic', 'disaster']
            },
            # ... (keeping existing scenes)
        ]
    },
    'climate_change': {
        'name': 'Climate Change Impact',
        'scenes': [
            {
                'id': 10,
                'title': 'Melting Glaciers',
                'prompt': 'Massive glacier calving into ocean, chunks falling, climate change, dramatic',
                'description': 'Ice sheets breaking due to warming',
                'tags': ['climate', 'ice', 'warming']
            },
            {
                'id': 11,
                'title': 'Rising Seas',
                'prompt': 'Coastal flooding, houses underwater, sea level rise, environmental disaster',
                'description': 'Communities lost to rising waters',
                'tags': ['flooding', 'coastal', 'rising-seas']
            }
        ]
    },
    'custom': {
        'name': 'Custom Creations', 
        'scenes': []
    }
}

@app.route('/')
def index():
    update_system_status()
    return render_template('enhanced_index.html', 
                         scene_categories=SCENE_CATEGORIES,
                         status=app_status)

@app.route('/models')
def models_page():
    return render_template('models.html', status=app_status)

@app.route('/system')
def system_page():
    update_system_status()
    return render_template('system.html', status=app_status)

@app.route('/custom')
def custom_page():
    return render_template('custom.html', status=app_status)

@app.route('/api/status')
def api_status():
    update_system_status()
    return jsonify(app_status)

@app.route('/api/download_model', methods=['POST'])
def download_model():
    model_id = request.json.get('model_id')
    
    # Find the model
    model = next((m for m in app_status['models']['available'] if m['id'] == model_id), None)
    if not model:
        return jsonify({'error': 'Model not found'})
    
    # Start download in background
    model['downloading'] = True
    thread = threading.Thread(target=download_model_worker, args=(model,))
    thread.start()
    
    return jsonify({'message': f'Started downloading {model["name"]}'})

@app.route('/api/create_custom_scene', methods=['POST'])
def create_custom_scene():
    data = request.json
    
    new_scene = {
        'id': len(SCENE_CATEGORIES['custom']['scenes']) + 100,
        'title': data.get('title', 'Custom Scene'),
        'prompt': data.get('prompt', ''),
        'description': data.get('description', ''),
        'tags': data.get('tags', []),
        'custom': True
    }
    
    SCENE_CATEGORIES['custom']['scenes'].append(new_scene)
    
    return jsonify({'message': 'Custom scene created', 'scene': new_scene})

@app.route('/api/generate_scene', methods=['POST'])
def generate_scene():
    scene_data = request.json
    
    # Add to generation queue
    app_status['generation']['queue'].append(scene_data)
    
    if not app_status['generation']['running']:
        thread = threading.Thread(target=generation_worker)
        thread.start()
    
    return jsonify({'message': 'Scene added to generation queue'})

@app.route('/api/update_settings', methods=['POST'])
def update_settings():
    new_settings = request.json
    app_status['settings'].update(new_settings)
    return jsonify({'message': 'Settings updated', 'settings': app_status['settings']})

def update_system_status():
    """Update real-time system information"""
    try:
        app_status['system'].update({
            'cpu_percent': psutil.cpu_percent(interval=0.1),
            'memory_percent': psutil.virtual_memory().percent,
            'disk_usage': psutil.disk_usage('.').percent,
            'uptime': time.time() - psutil.boot_time(),
            'active_processes': len(psutil.pids())
        })
    except:
        pass

def download_model_worker(model):
    """Download and install a model"""
    try:
        # Simulate download progress
        for i in range(101):
            time.sleep(0.1)  # Simulate download time
            model['download_progress'] = i
        
        model['downloading'] = False
        model['installed'] = True
        
        # Set as active model if it's the first one installed
        if not app_status['models']['active_model']:
            app_status['models']['active_model'] = model['id']
            
    except Exception as e:
        model['downloading'] = False
        model['error'] = str(e)

def generation_worker():
    """Process the generation queue"""
    app_status['generation']['running'] = True
    
    while app_status['generation']['queue']:
        current_scene = app_status['generation']['queue'].pop(0)
        
        app_status['generation']['message'] = f"Generating: {current_scene.get('title', 'Custom Scene')}"
        
        # Simulate generation process
        for i in range(101):
            time.sleep(0.2)  # Simulate processing
            app_status['generation']['progress'] = i
        
        # Mark as completed
        timestamp = datetime.now().strftime("%H%M%S")
        app_status['generation']['completed_videos'].append({
            'title': current_scene.get('title', 'Custom Scene'),
            'filename': f"video_{timestamp}.mp4",
            'timestamp': timestamp,
            'prompt': current_scene.get('prompt', ''),
            'settings': app_status['settings'].copy()
        })
        
        app_status['generation']['progress'] = 0
    
    app_status['generation']['running'] = False
    app_status['generation']['message'] = 'All generations completed!'

if __name__ == '__main__':
    print("Enhanced Ocean Video Generator")
    print("=" * 50)
    print("Starting advanced web interface...")
    print("Open: http://localhost:5000")
    print("Features: Model management, system monitoring, custom scenes")
    print()
    
    # Create required directories
    os.makedirs('templates', exist_ok=True)
    os.makedirs('static', exist_ok=True)
    os.makedirs('models', exist_ok=True)
    os.makedirs('outputs', exist_ok=True)
    
    app.run(debug=True, host='localhost', port=5000)
