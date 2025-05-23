"""
Ocean Pollution Video Generator - Simple Version
Uses Hugging Face Diffusers for text-to-video generation
"""

import torch
import os
from diffusers import DiffusionPipeline
from datetime import datetime

def setup_environment():
    """Setup the video generation environment"""
    
    print("🔧 Setting up AI video generation...")
    
    # Check if we have GPU support
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"💻 Using device: {device}")
    
    if device == "cpu":
        print("⚠️  Running on CPU - generation will be slower but works!")
    
    return device

def generate_scene_video(prompt, scene_number=1, output_dir="ocean_videos"):
    """Generate a single 6-second video scene"""
    
    device = setup_environment()
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    print(f"🎬 Generating Scene {scene_number}")
    print(f"📝 Prompt: {prompt[:100]}...")
    
    try:
        # Load a simpler text-to-video model
        print("⬇️  Loading model (first time may take 5-10 minutes)...")
        
        # Use a lightweight model for CPU
        pipe = DiffusionPipeline.from_pretrained(
            "damo-vilab/text-to-video-ms-1.7b",
            torch_dtype=torch.float16 if device == "cuda" else torch.float32,
            variant="fp16" if device == "cuda" else None
        )
        pipe = pipe.to(device)
        
        print("✅ Model loaded! Generating video...")
        
        # Generate video
        video_frames = pipe(
            prompt,
            num_inference_steps=25,
            num_frames=48,  # 6 seconds at 8fps
            guidance_scale=9.0,
            width=512,
            height=512
        ).frames[0]
        
        # Save video
        timestamp = datetime.now().strftime("%H%M%S")
        output_path = os.path.join(output_dir, f"scene_{scene_number:02d}_{timestamp}.mp4")
        
        # Export frames to video
        export_to_video(video_frames, output_path, fps=8)
        
        print(f"✅ Scene {scene_number} saved: {output_path}")
        return output_path
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("💡 Try: pip install diffusers[torch] transformers accelerate")
        return None

def export_to_video(frames, output_path, fps=8):
    """Export frames to MP4 video"""
    try:
        import cv2
        import numpy as np
        
        # Convert PIL images to OpenCV format
        cv2_frames = []
        for frame in frames:
            frame_np = np.array(frame)
            frame_bgr = cv2.cvtColor(frame_np, cv2.COLOR_RGB2BGR)
            cv2_frames.append(frame_bgr)
        
        # Write video
        height, width, _ = cv2_frames[0].shape
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
        
        for frame in cv2_frames:
            out.write(frame)
        
        out.release()
        
    except ImportError:
        print("❌ OpenCV not found. Installing...")
        os.system("pip install opencv-python")
        export_to_video(frames, output_path, fps)

if __name__ == "__main__":
    print("🌊 OCEAN POLLUTION VIDEO GENERATOR")
    print("=" * 50)
    
    # Test generation
    test_prompt = "Pristine blue ocean waters at sunrise, cinematic aerial view"
    generate_scene_video(test_prompt, scene_number=1)
